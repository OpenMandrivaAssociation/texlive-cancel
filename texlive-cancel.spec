%global tl_name cancel
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Place lines through maths formulae
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cancel
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cancel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cancel.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package to draw diagonal lines ("cancelling" a term) and arrows with
limits (cancelling a term "to a value") through parts of maths formulae.

