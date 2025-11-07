#!/usr/bin/env python3
"""
NebulaOS Supervisor
Core backend daemon for monitoring and service orchestration.
"""

from fastapi import FastAPI
import psutil

app = FastAPI(
    title="NebulaOS Supervisor",
    description="Backend API for NebulaOS server monitoring and service management",
    version="0.1.0",
)

# ---------------------------
# Health / stats endpoints
# ---------------------------

@app.get("/stats")
def get_stats():
    """
    Returns basic system stats: CPU, RAM, disk, network, temperature
    """
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram": {
            "total": psutil.virtual_memory().total,
            "available": psutil.virtual_memory().available,
            "percent": psutil.virtual_memory().percent
        },
        "disk": [
            {
                "mountpoint": partition.mountpoint,
                "total": psutil.disk_usage(partition.mountpoint).total,
                "used": psutil.disk_usage(partition.mountpoint).used,
                "percent": psutil.disk_usage(partition.mountpoint).percent
            } for partition in psutil.disk_partitions()
        ],
        "network": psutil.net_io_counters()._asdict()
    }

# ---------------------------
# Placeholder service endpoints
# ---------------------------

@app.get("/services")
def list_services():
    """
    List all managed services and their status
    """
    # TODO: Implement real service detection
    return {
        "ssh": "running",
        "samba": "stopped",
        "docker": "running",
        "backup": "stopped"
    }

# ---------------------------
# Main entry point
# ---------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
