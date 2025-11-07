# NebulaOS

NebulaOS is a lightweight, modular home server operating system designed for Raspberry Pi and Debian-based systems. Inspired by projects like TrueNAS and OpenMediaVault, NebulaOS empowers users to monitor, manage, and extend their servers—completely offline and with full user ownership.

## Goals

- **Local-first**: All features work fully offline. Data stays on your hardware.
- **Modern web dashboard**: Responsive and accessible UI for both mobile and desktop.
- **System monitoring**: View CPU, RAM, disk, network, and temperature stats.
- **Service manager**: Easily enable or disable core services (SSH, Samba, Docker, backup, etc).
- **Plugin architecture**: Community-driven, enable new features through modular plugins.
- **User privacy**: No telemetry, no vendor lock-in, all operations are local.

## Repository Structure

- `supervisor/` — Core backend daemon for monitoring and service orchestration.
- `web-dashboard/` — Web dashboard for managing the OS from any browser.
- `docs/` — Documentation and technical references.
- `installer/` — Install scripts, systemd units, and images for Pi/x86 systems.
- `plugins/` — Example and built-in plugins to extend NebulaOS capabilities.
- `tests/` — End-to-end, integration, and unit tests, including CI routines.
- `.github/workflows/` — CI/CD pipeline definitions for automated testing and builds.

---

NebulaOS is open source and welcomes feedback and community contributions!
