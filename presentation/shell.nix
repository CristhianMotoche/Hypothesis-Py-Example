{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    buildInputs = [ pkgs.nodejs pkgs.npm2nix ];

    shellHook =
      ''
      $SHELL ./setup.sh
      '';
  }
