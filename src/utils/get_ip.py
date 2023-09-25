from fastapi import Request

async def remote(request: Request) -> str:
    client_ip = request.headers.get("x-real-ip")
    if client_ip is None:
        forwarded_for = request.headers.get("x-forwarded-for")
        if forwarded_for is not None:
            # O cabeçalho 'x-forwarded-for' pode conter uma lista de IPs
            # O primeiro é o original. Os outros são os IPs dos servidores intermediários.
            client_ip = forwarded_for.split(",")[0]
    if client_ip is None:
        return None
    return client_ip
