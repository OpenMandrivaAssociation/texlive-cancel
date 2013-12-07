# revision 17124
# category Package
# catalog-ctan /macros/latex/contrib/cancel
# catalog-date 2010-02-23 16:16:11 +0100
# catalog-license pd
# catalog-version 2.0
Name:		texlive-cancel
Version:	2.0
Release:	4
Summary:	Place lines through maths formulae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cancel
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cancel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cancel.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 749968
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 718000
- texlive-cancel
- texlive-cancel
- texlive-cancel
- texlive-cancel
- texlive-cancel

