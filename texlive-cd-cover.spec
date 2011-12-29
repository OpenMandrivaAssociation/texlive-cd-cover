# revision 17121
# category Package
# catalog-ctan /macros/latex/contrib/cd-cover
# catalog-date 2010-02-21 01:36:59 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-cd-cover
Version:	1.0
Release:	1
Summary:	Typeset CD covers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cd-cover
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd-cover.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd-cover.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd-cover.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The CD-cover class will typeset front and back cover sheets for
CD jewel cases, or an entire paper cover, or a label for a
plastic slip-cover.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cd-cover/cd-cover.cls
%doc %{_texmfdistdir}/doc/latex/cd-cover/README
%doc %{_texmfdistdir}/doc/latex/cd-cover/cd-cover.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cd-cover/cd-cover.dtx
%doc %{_texmfdistdir}/source/latex/cd-cover/cd-cover.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
