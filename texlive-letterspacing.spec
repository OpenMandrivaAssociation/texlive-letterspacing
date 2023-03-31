Name:		texlive-letterspacing
Version:	54266
Release:	2
Summary:	Letter spacing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/letterspacing
License:	knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/letterspacing.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Space out the letters of text; the command is
\letterspace<\hbox modifier>{<text>}: the text is placed in an
\hbox of the specified size, and space is inserted between each
glyph to make the text fit the box. Note that letterspacing is
not ordinarily considered acceptable in modern typesetting of
English.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/letterspacing

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
