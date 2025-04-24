# Redshift MCP Server

A Model Context Protocol (MCP) server for Amazon Redshift that enables AI assistants to interact with Redshift databases.

## Introduction

Redshift MCP Server is a Python-based implementation of the [Model Context Protocol](https://github.com/modelcontextprotocol/mcp) that provides tools and resources for interacting with Amazon Redshift databases. It allows AI assistants to:

- List schemas and tables in a Redshift database
- Retrieve table DDL (Data Definition Language) scripts
- Get table statistics
- Execute SQL queries
- Analyze tables to collect statistics information
- Get execution plans for SQL queries

## Installation

### Prerequisites

- Python 3.13 or higher
- Amazon Redshift cluster
- Redshift credentials (host, port, username, password, database)

### Install from source

```bash
# Clone the repository
git clone https://github.com/aws-samples/sample-amazon-redshift-MCP-server.git
cd sample-amazon-redshift-MCP-server

# Install dependencies
uv sync
```

## Configuration

The server requires the following environment variables to connect to your Redshift cluster:

```
RS_HOST=your-redshift-cluster.region.redshift.amazonaws.com
RS_PORT=5439
RS_USER=your_username
RS_PASSWORD=your_password
RS_DATABASE=your_database
RS_SCHEMA=your_schema  # Optional, defaults to "public"
```

## Usage

### Integrating with AI assistants

To use this server with an AI assistant that supports MCP, add the following configuration to your MCP settings:

```json
{
  "mcpServers": {
    "redshift": {
      "command": "uv",
      "args": ["--directory", "src/redshift_mcp_server", "run", "server.py"],
      "env": {
        "RS_HOST": "your-redshift-cluster.region.redshift.amazonaws.com",
        "RS_PORT": "5439",
        "RS_USER": "your_username",
        "RS_PASSWORD": "your_password",
        "RS_DATABASE": "your_database",
        "RS_SCHEMA": "your_schema"
      }
    }
  }
}
```

## Features

### Resources

The server provides the following resources:

- `rs:///schemas` - Lists all schemas in the database
- `rs:///{schema}/tables` - Lists all tables in a specific schema
- `rs:///{schema}/{table}/ddl` - Gets the DDL script for a specific table
- `rs:///{schema}/{table}/statistic` - Gets statistics for a specific table

### Tools

The server provides the following tools:

- `execute_sql` - Executes a SQL query on the Redshift cluster
- `analyze_table` - Analyzes a table to collect statistics information
- `get_execution_plan` - Gets the execution plan with runtime statistics for a SQL query

## Examples

### Listing schemas

```
access_mcp_resource("redshift-mcp-server", "rs:///schemas")
```

### Listing tables in a schema

```
access_mcp_resource("redshift-mcp-server", "rs:///public/tables")
```

### Getting table DDL

```
access_mcp_resource("redshift-mcp-server", "rs:///public/users/ddl")
```

### Executing SQL

```
use_mcp_tool("redshift-mcp-server", "execute_sql", {"sql": "SELECT * FROM public.users LIMIT 10"})
```

### Analyzing a table

```
use_mcp_tool("redshift-mcp-server", "analyze_table", {"schema": "public", "table": "users"})
```

### Getting execution plan

```
use_mcp_tool("redshift-mcp-server", "get_execution_plan", {"sql": "SELECT * FROM public.users WHERE user_id = 123"})
```

## Development

### Project structure

```
redshift-mcp-server/
├── src/
│   └── redshift_mcp_server/
│       ├── __init__.py
│       └── server.py
├── pyproject.toml
└── README.md
```

### Dependencies

- `mcp[cli]>=1.5.0` - Model Context Protocol SDK
- `python-dotenv>=1.1.0` - For loading environment variables from .env files
- `redshift-connector>=2.1.5` - Python connector for Amazon Redshift
