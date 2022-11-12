Name:		texlive-cd-cover
Version:	17121
Release:	1
Summary:	Typeset CD covers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cd-cover
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd-cover.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd-cover.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd-cover.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
