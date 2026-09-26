# Architecture

The `dsa` target is an interface library: implementations live in headers and
clients include only the features they use. Tests and the demo are separate
executables linked to the same target.
