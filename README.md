# pythoneda-sandbox/python-dep-artifact

Artifact space for <https://github.com/pythoneda-sandbox/python-dep>

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-sandbox/python-dep-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-sandbox-python-dep = {
      [optional follows]
      url =
        "github:pythoneda-sandbox/python-dep-artifact/[version]?dir=python-dep";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-sandbox/python-dep-artifact/tree/main/python-dep](python-dep "python-dep") folder of <https://github.com/pythoneda-sandbox/python-dep-artifact>.


