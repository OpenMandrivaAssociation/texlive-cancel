Name:		texlive-cancel
Version:	32508
Release:	2
Summary:	Place lines through maths formulae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cancel
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cancel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cancel.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to draw diagonal lines ("cancelling" a term) and
arrows with limits (cancelling a term "to a value") through
parts of maths formulae.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cancel/cancel.sty
%doc %{_texmfdistdir}/doc/latex/cancel/cancel.pdf
%doc %{_texmfdistdir}/doc/latex/cancel/cancel.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
