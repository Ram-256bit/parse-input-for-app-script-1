{
  pkgs ? import <nixpkgs> { },
}:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python312
    python312Packages.tkinter
    python312Packages.pyinstaller
  ];

}
