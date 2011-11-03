# revision 17124
# category Package
# catalog-ctan /macros/latex/contrib/cancel
# catalog-date 2010-02-23 16:16:11 +0100
# catalog-license pd
# catalog-version 2.0
Name:		texlive-cancel
Version:	2.0
Release:	1
Summary:	Place lines through maths formulae
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cancel
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cancel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cancel.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A package to draw diagonal lines ("cancelling" a term) and
arrows with limits (cancelling a term "to a value") through
parts of maths formulae.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cancel/cancel.sty
%doc %{_texmfdistdir}/doc/latex/cancel/cancel.pdf
%doc %{_texmfdistdir}/doc/latex/cancel/cancel.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
