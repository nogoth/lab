import asyncio
import json
import argparse
import random
from typing import Optional

SHAKESPEARE_QUOTES = [
    "All the world's a stage, and all the men and women merely players.",
    "To be, or not to be, that is the question.",
    "The course of true love never did run smooth.",
    "What's in a name? A rose by any other name would smell as sweet.",
    "We know what we are, but know not what we may be.",
    "Love all, trust a few, do wrong to none.",
    "Better three hours too soon than a minute too late.",
    "All that glitters is not gold.",
]


async def handle_request(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    try:
        # Read the request line
        request_line = await reader.readline()
        method, path, _ = request_line.decode().strip().split(" ")

        # Read headers until we hit empty line
        headers = {}
        while True:
            line = await reader.readline()
            if line == b"\r\n":
                break
            if not line:
                break
            name, value = line.decode().strip().split(":", 1)
            headers[name.strip().lower()] = value.strip()

        match method:
            case "GET":
                # do get stuff
                if path == "/health":
                    response_data = {"status": "healthy", "timestamp": "2025-10-24"}
                    status = "200 OK"
                elif path == "/Status":
                    response_data = {
                        "status": "healthy",
                        "shakespeare_wisdom": random.choice(SHAKESPEARE_QUOTES),
                    }
                    status = "200 OK"
            case "POST":
                # post stuff here
                # Read content length if present
                content_length = int(headers.get("content-length", 0))
                if content_length > 0:
                    # Read the body if there is one
                    await reader.read(content_length)

                response_data = {"status": "ok"}
                status = "200 OK"

            case _:
                # default to nah
                response_data = {"error": "not found"}
                status = "404 Not Found"

        # Send response
        response = json.dumps(response_data)
        response_headers = [
            f"HTTP/1.1 {status}",
            "Content-Type: application/json",
            f"Content-Length: {len(response)}",
            "Connection: close",
            "",
            response,
        ]
        writer.write("\r\n".join(response_headers).encode())
        await writer.drain()

    except Exception as e:
        # Send error response if something goes wrong
        error_response = json.dumps({"error": str(e)})
        error_headers = [
            "HTTP/1.1 500 Internal Server Error",
            "Content-Type: application/json",
            f"Content-Length: {len(error_response)}",
            "Connection: close",
            "",
            error_response,
        ]
        writer.write("\r\n".join(error_headers).encode())
        await writer.drain()

    finally:
        writer.close()
        await writer.wait_closed()


async def run_server(host: str = "", port: int = 8080):
    server = await asyncio.start_server(handle_request, host, port)
    print(f"Server running on {host or '0.0.0.0'}:{port}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Async HTTP Server")
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8080,
        help="Port to run the server on (default: 8080)",
    )
    args = parser.parse_args()

    asyncio.run(run_server(port=args.port))
