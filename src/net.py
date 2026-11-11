def parse_port(s):
    """Parse a TCP port string; reject values outside 1-65535."""
    p = int(s)
    if p < 1 or p > 65535:
        raise ValueError("port out of range")
    return p
