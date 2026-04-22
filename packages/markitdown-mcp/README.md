# MarkItDown-MCP

> [!IMPORTANT]
> The MarkItDown-MCP package is meant for **local use**, with local trusted agents. In particular, when running the MCP server with Streamable HTTP or SSE, it binds to `localhost` by default, and is not exposed to other machines on the network or Internet. In this configuration, it is meant to be a direct alternative to the STDIO transport, which may be more convenient in some cases. DO NOT bind the server to other interfaces unless you understand the [security implications](#security-considerations) of doing so.


[![PyPI](https://img.shields.io/pypi/v/markitdown-mcp.svg)](https://pypi.org/project/markitdown-mcp/)
![PyPI - Downloads](https://img.shields.io/pypi/dd/markitdown-mcp)
[![Built by AutoGen Team](https://img.shields.io/badge/Built%20by-AutoGen%20Team-blue)](https://github.com/microsoft/autogen)

The `markitdown-mcp` package provides a lightweight STDIO, Streamable HTTP, and SSE MCP server for calling MarkItDown.

It exposes one tool: `convert_to_markdown(content_base64, filename=None, extension=None, mimetype=None, charset=None, url=None)`.

The client must send the file bytes as a base64-encoded string. The optional metadata fields help MarkItDown infer the correct converter, especially for formats that depend on filename extension or MIME type.

Example tool arguments:

```json
{
  "content_base64": "PGh0bWw+PGJvZHk+PGgxPkV4YW1wbGU8L2gxPjwvYm9keT48L2h0bWw+",
  "filename": "example.html",
  "mimetype": "text/html",
  "charset": "utf-8",
  "url": "https://example.com/example.html"
}
```

## Installation

To install the package, use pip:

```bash
pip install markitdown-mcp
```

## Usage

To run the MCP server, using STDIO (default), use the following command:


```bash
markitdown-mcp
```

To run the MCP server, using Streamable HTTP and SSE, use the following command:

```bash
markitdown-mcp --http --host 127.0.0.1 --port 3001
```

## Running in Docker

To run `markitdown-mcp` in Docker, build the Docker image using the provided Dockerfile:
```bash
docker build -t markitdown-mcp:latest .
```

And run it using:
```bash
docker run -it --rm markitdown-mcp:latest
```

No local directory mount is required for uploaded content. The client sends the file bytes to the MCP server as part of the tool arguments.

## Accessing from Claude Desktop

It is recommended to use the Docker image when running the MCP server for Claude Desktop.

Follow [these instructions](https://modelcontextprotocol.io/quickstart/user#for-claude-desktop-users) to access Claude's `claude_desktop_config.json` file.

Edit it to include the following JSON entry:

```json
{
  "mcpServers": {
    "markitdown": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "markitdown-mcp:latest"
      ]
    }
  }
}
```

## Using an mcp-config.json File for HTTP

If you are running `markitdown-mcp` with Streamable HTTP enabled, for example via:

```bash
docker compose up --build
```

you can point MCP clients that support config files at the HTTP endpoint with an `mcp-config.json` file like this:

```json
{
  "mcpServers": {
    "markitdown": {
      "type": "streamable-http",
      "url": "http://127.0.0.1:3001/mcp"
    }
  }
}
```

If you expose the server on a different host or port, update the `url` accordingly.

## Debugging

To debug the MCP server you can use the `MCP Inspector` tool.

```bash
npx @modelcontextprotocol/inspector
```

You can then connect to the inspector through the specified host and port (e.g., `http://localhost:5173/`).

If using STDIO:
* select `STDIO` as the transport type,
* input `markitdown-mcp` as the command, and
* click `Connect`

If using Streamable HTTP:
* select `Streamable HTTP` as the transport type,
* input `http://127.0.0.1:3001/mcp` as the URL, and
* click `Connect`

If using SSE:
* select `SSE` as the transport type,
* input `http://127.0.0.1:3001/sse` as the URL, and
* click `Connect`

Finally:
* click the `Tools` tab,
* click `List Tools`,
* click `convert_to_markdown`, and
* run the tool with a base64-encoded file payload and any useful metadata.

## Security Considerations

The server does not support authentication, and runs with the privileges of the user running it. For this reason, when running in SSE or Streamable HTTP mode, the server binds by default to `localhost`. Even still, it is important to recognize that the server can be accessed by any process or users on the same local machine, and that the `convert_to_markdown` tool will process arbitrary file content supplied by clients. If you require additional security, consider running the server in a sandboxed environment, such as a virtual machine or container, and ensure that the user permissions are properly configured to limit the impact of processing untrusted files. Above all, DO NOT bind the server to other interfaces (non-localhost) unless you understand the security implications of doing so.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
