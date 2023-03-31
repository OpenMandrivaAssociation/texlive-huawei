Name:		texlive-huawei
Version:	65264
Release:	2
Summary:	Template for Huawei documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/huawei
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/huawei.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/huawei.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/huawei.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This unofficial package provides a class for creating documents
for people working with Huawei Technologies Co., Ltd.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/huawei
%{_texmfdistdir}/tex/latex/huawei
%doc %{_texmfdistdir}/doc/latex/huawei

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
