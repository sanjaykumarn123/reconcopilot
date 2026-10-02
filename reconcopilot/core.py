from .parsers.subfinder import parse_subfinder
from .parsers.httpx import parse_httpx
from .db import SessionLocal
from .models import Target, Endpoint

PARSERS = {
    "subfinder": parse_subfinder,
    "httpx": parse_httpx,
    # "katana": parse_katana,   # next
    # "nuclei": parse_nuclei,   # next
    # "burp": parse_burp,       # next
}

def ingest_file(filepath: str, source: str, target_name: str) -> int:
    if source not in PARSERS:
        raise ValueError(f"Unsupported source: {source}. Choose from {list(PARSERS)}")

    parsed = PARSERS[source](filepath)

    db = SessionLocal()
    try:
        target = db.query(Target).filter_by(program_name=target_name).first()
        if not target:
            target = Target(program_name=target_name)
            db.add(target)
            db.commit()
            db.refresh(target)

        for item in parsed:
            db.add(Endpoint(target_id=target.id, **item))
        db.commit()
        return len(parsed)
    finally:
        db.close()