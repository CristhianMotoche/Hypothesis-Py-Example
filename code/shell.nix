{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    buildInputs = [ pkgs.pipenv ];

    shellHook =
      ''
      $SHELL ./setup.sh
      '';
  }
