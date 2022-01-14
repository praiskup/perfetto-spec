Name:           perfetto
Version:        22.1
Release:        1%{?dist}
Summary:        System profiling, app tracing and trace analysis tool.

License:        Apache License 2.0
URL:            https://github.com/google/%{name}
Source0:        https://github.com/google/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

#gn needs this
BuildRequires:	openssl >= 1.0

BuildRequires:  gn
BuildRequires:  ninja-build
BuildRequires:  gcc python
BuildRequires:  clang llvm-googletest
BuildRequires:  clang-tools-extra
BuildRequires:  protobuf-devel
BuildRequires:  libcxx libcxxabi
BuildRequires:  sqlite jsoncpp bloaty linenoise protobuf libcxx libcxxabi libunwind lzma zlib
#BuildRequires:  sqlite_src bionic libfuzzer benchmark libbacktrace googletest clang-format
#BuildRequires:  android-core android-unwinding android-libbase android-libprocinfo android-logging

%description
Perfetto is a production-grade open-source stack for performance
instrumentation and trace analysis. It offers services and libraries and for
recording system-level and app-level traces, native + java heap profiling, a
library for analyzing traces using SQL and a web-based UI to visualize and
explore multi-GB traces.

%prep
%autosetup -p1


%build
gn gen --args='is_debug=false' out/linux
%ninja_build -C out/linux tracebox traced traced_probes perfetto


%install
%ninja_install


%files
%license LICENSE
%{_bindir}/%{name}
%doc README.md
%doc CHANGELOG
%doc OWNERS
%doc docs
%doc examples
%doc infra
%doc tools



%changelog
* Wed Jan 12 2022 Dorinda Bassey <dbassey@redhat.com> -22.1-1
- Initial Packaged Version
