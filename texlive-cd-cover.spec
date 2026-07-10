%global tl_name cd-cover
%global tl_revision 17121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typeset CD covers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cd-cover
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cd-cover.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cd-cover.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cd-cover.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The CD-cover class will typeset front and back cover sheets for CD jewel
cases, or an entire paper cover, or a label for a plastic slip-cover.

