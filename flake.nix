{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }: flake-utils.lib.eachDefaultSystem (system: let
    pkgs = nixpkgs.legacyPackages.${system};
    
    mypyenv = pkgs.python3.withPackages (ps: with ps; [
      pytest
    ]);

  in {
    devShell = pkgs.mkShell {
      packages = with pkgs; [
        mypyenv
        pkgs.bash
        pkgs.gitAndTools.git
      ];
    };
  });
}

