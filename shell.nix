{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    buildInputs = [ pkgs.pipenv pkgs.nodejs ];

    shellHook =
      ''
      $SHELL ./setup.sh
      '';
  }
