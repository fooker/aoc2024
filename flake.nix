{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system: let
    pkgs = nixpkgs.legacyPackages.${system};
    
    mypyenv = pkgs.python312.withPackages (ps: with ps; [
      pytest
      numpy
    ]);

  in {
    devShell = pkgs.mkShell {
      packages = [
        mypyenv
        pkgs.bash
        pkgs.gitAndTools.git
      ];
    };
  });
}

