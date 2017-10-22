Name: oauth2_proxy
Version: 2.2.0
Release: 1
Summary: oauth2_proxy binary
License: MIT
Requires: sysvinit
URL: https://github.com/bitly/oauth2_proxy
Source0: https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-%{version}.linux-amd64.go1.8.1.tar.gz
Source1: https://raw.githubusercontent.com/bitly/oauth2_proxy/master/contrib/oauth2_proxy.cfg.example
Source2: https://raw.githubusercontent.com/alediaferia/oauth2_proxy-sysv-init/master/oauth2_proxy-sysv-init

%description
oauth2_proxy binary package

%prep
%setup -q -c -n oauth2_proxy-%{version}.linux-amd64.go1.8.1
cp -p %{SOURCE1} %{_builddir}/oauth2_proxy-%{version}.linux-amd64.go1.8.1/
cp -p %{SOURCE2} %{_builddir}/oauth2_proxy-%{version}.linux-amd64.go1.8.1/

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/oauth2_proxy
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -p -m 755 oauth2_proxy-%{version}.linux-amd64.go1.8.1/oauth2_proxy %{buildroot}%{_bindir}/
install -p -m 755 oauth2_proxy-sysv-init %{buildroot}%{_sysconfdir}/init.d/oauth2_proxy
install -p oauth2_proxy.cfg.example %{buildroot}%{_sysconfdir}/oauth2_proxy/

%files
%{_bindir}/oauth2_proxy
%config %{_sysconfdir}/oauth2_proxy/*.cfg.example
%config %{_sysconfdir}/init.d/oauth2_proxy

%clean
rm -rf %{buildroot}
