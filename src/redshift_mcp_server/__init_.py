from . import server
import asyncio

def main():
    """Entry point"""
    asyncio.run(server.run())

__all__= ['main', 'server']
