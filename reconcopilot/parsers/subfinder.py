def parse_subfinder(filepath: str) -> list[dict]:
    """
    Subfinder output: one subdomain per line, plain text.
    e.g.:
        api.example.com
        dev.example.com
    """
    endpoints = []
    with open(filepath) as f:
        for line in f:
            host = line.strip()
            if not host:
                continue
            endpoints.append({
                "host": host,
                "url": None,
                "status_code": None,
                "title": None,
                "tech_stack": None,
                "source_tool": "subfinder",
            })
    return endpoints