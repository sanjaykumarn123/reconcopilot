import json

def parse_httpx(filepath: str) -> list[dict]:
    """
    httpx output: JSON Lines (one JSON object per line).
    Generate with: httpx -l subdomains.txt -json -o out.jsonl -title -tech-detect -status-code
    """
    endpoints = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            tech = data.get("tech", [])
            endpoints.append({
                "host": data.get("input") or data.get("host"),
                "url": data.get("url"),
                "status_code": data.get("status_code"),
                "title": data.get("title"),
                "tech_stack": ", ".join(tech) if tech else None,
                "source_tool": "httpx",
            })
    return endpoints