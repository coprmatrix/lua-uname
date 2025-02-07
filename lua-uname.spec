%define luarocks_pkg_name uname
%define luarocks_pkg_version 1.21-1
%define luarocks_pkg_prefix uname-1.21-1
%define luarocks_pkg_major 1.21
%define luarocks_pkg_minor 1

Name: lua-uname
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: C module for Lua for getting distribution information
Url: http://github.com/huakim/lua-uname
License: MIT/X11
Source0: uname-1.21-1.tar.gz
Source1: uname-1.21-1.rockspec
BuildRequires: lua-rpm-macros
Requires(postun): alternatives
Requires(post): alternatives
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true
Requires: %{luadist lua >= 5.1}
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
    Lua module written in C, which gets distribution information.
  

%prep
%autosetup -p1 -n %{luarocks_pkg_prefix}
%luarocks_prep

%generate_buildrequires
%{?luarocks_buildrequires_echo}
%if %{with check}
%luarocks_generate_buildrequires -c -b
%else
%luarocks_generate_buildrequires -b 
%endif

%build
%{?custom_build}
%if %{defined luarocks_subpackages_build}
%{luarocks_subpackages_build}
%else
%if %{defined luarocks_pkg_build}
%luarocks_pkg_build %{lua_version}
%else
%luarocks_build --local
%endif
%endif

%install
%{?custom_install}
%if %{defined luarocks_subpackages_install}
%{luarocks_subpackages_install}
%else
%if %{defined luarocks_pkg_install}
%luarocks_pkg_install %{lua_version}
%else
%luarocks_install %{luarocks_pkg_prefix}.*.rock
%endif
%endif
%{?lua_generate_file_list}

%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}
