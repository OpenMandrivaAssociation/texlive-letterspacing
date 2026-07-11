%global tl_name letterspacing
%global tl_revision 54266

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Letter spacing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/misc/letterspacing.tex
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/letterspacing.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Space out the letters of text; the command is \letterspace<\hbox
modifier>{<text>}: the text is placed in an \hbox of the specified size,
and space is inserted between each glyph to make the text fit the box.
Note that letterspacing is not ordinarily considered acceptable in
modern typesetting of English.

