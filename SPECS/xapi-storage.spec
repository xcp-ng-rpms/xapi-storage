Summary:       Xapi storage interface
Name:          xapi-storage
Version:       8.19.0_sxm2
Release:       2%{?dist}
URL:           https://github.com/xapi-project/xapi-storage

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xapi-storage/archive?at=v8.19.0_sxm2&format=tar.gz&prefix=xapi-storage-8.19.0_sxm2#/xapi-storage-8.19.0_sxm2.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xapi-storage/archive?at=v8.19.0_sxm2&format=tar.gz&prefix=xapi-storage-8.19.0_sxm2#/xapi-storage-8.19.0_sxm2.tar.gz) = c1e0780edf84b06f0778fdb49c69ac6b909612f4

License:       LGPL+linking exception
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: xs-opam-repo

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Xapi storage inteface libraries

%package        ocaml-plugin-runtime
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xapi-storage/archive?at=v8.19.0_sxm2&format=tar.gz&prefix=xapi-storage-8.19.0_sxm2#/xapi-storage-8.19.0_sxm2.tar.gz) = c1e0780edf84b06f0778fdb49c69ac6b909612f4
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    ocaml-plugin-runtime
The %{name}-ocaml-plugin package contains runtime libraries for OCaml
plugins for %{name}.

%package        ocaml-plugin-devel
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xapi-storage/archive?at=v8.19.0_sxm2&format=tar.gz&prefix=xapi-storage-8.19.0_sxm2#/xapi-storage-8.19.0_sxm2.tar.gz) = c1e0780edf84b06f0778fdb49c69ac6b909612f4
Summary:        Development files for %{name}
Requires:       %{name}-ocaml-plugin-runtime = %{version}-%{release}
Requires:       xs-opam-repo

%description    ocaml-plugin-devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%global ocaml_dir    %{_opamroot}/ocaml-system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc

%build
make

%check
make test

%install
mkdir -p %{buildroot}%{ocaml_libdir}
mkdir -p %{buildroot}%{ocaml_docdir}
make install OPAM_PREFIX=%{buildroot}%{ocaml_dir} OPAM_LIBDIR=%{buildroot}%{ocaml_libdir} PYTHON_PREFIX=%{buildroot}/usr

%files
%defattr(-,root,root,-)
%{python_sitelib}/xapi/__init__.py*
%{python_sitelib}/xapi/storage/__init__.py*
%{python_sitelib}/xapi/storage/common.py*
%{python_sitelib}/xapi/storage/log.py*
%{python_sitelib}/xapi/storage/api/datapath.py*
%{python_sitelib}/xapi/storage/api/volume.py*
%{python_sitelib}/xapi/storage/api/plugin.py*
%{python_sitelib}/xapi/storage/api/__init__.py*
%{python_sitelib}/xapi/storage/api/v5/datapath.py*
%{python_sitelib}/xapi/storage/api/v5/volume.py*
%{python_sitelib}/xapi/storage/api/v5/plugin.py*
%{python_sitelib}/xapi/storage/api/v5/task.py*
%{python_sitelib}/xapi/storage/api/v5/__init__.py*
%exclude %{python_sitelib}/*.egg-info

%files ocaml-plugin-runtime
%defattr(-,root,root,-)
%{ocaml_libdir}/xapi-storage/*
%exclude %{ocaml_libdir}/xapi-storage/*.a
%exclude %{ocaml_libdir}/xapi-storage/*.cmt
%exclude %{ocaml_libdir}/xapi-storage/*.cmx
%exclude %{ocaml_libdir}/xapi-storage/*.cmxa
%exclude %{ocaml_libdir}/xapi-storage/*.ml

%files ocaml-plugin-devel
%defattr(-,root,root,-)
%{ocaml_docdir}/xapi-storage/*
%{ocaml_libdir}/xapi-storage/*
%exclude %{ocaml_libdir}/xapi-storage/*.cma
%exclude %{ocaml_libdir}/xapi-storage/*.cmi
%exclude %{ocaml_libdir}/xapi-storage/*.cmt
%exclude %{ocaml_libdir}/xapi-storage/*.cmxs
%exclude %{ocaml_libdir}/xapi-storage/*.ml

%changelog
* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 8.19.0_sxm2-2
- bump packages after xs-opam update

* Fri Aug 02 2019 Christian Lindig <christian.lindig@citrix.com> - 8.19.0_sxm2-1
- Fix unit tests
- Update opam file from xs-opam

* Wed Mar 20 2019 Christian Lindig <christian.lindig@citrix.com> - 7.19.0_sxm2-1
- CA-306713: expose log.critical method

* Fri Feb 01 2019 Christian Lindig <christian.lindig@citrix.com> - 6.19.0_sxm2-1
- Replaced jbuild files with dune.
- Disabled broken tests temporarily until they are updated.

* Fri Nov 16 2018 Christian Lindig <christian.lindig@citrix.com> - 5.19.0_sxm2-1
- doc,plugin: All plugins need to satisfy interface

* Thu Nov 01 2018 Christian Lindig <christian.lindig@citrix.com> - 4.19.0_sxm2-1
- Update opam files for Opam 2, move Travis to OCaml 4.06

* Wed Sep 05 2018 Christian Lindig <christian.lindig@citrix.com> - 3.19.0_sxm2-1
- Simplify PPX processing in jbuild file

* Mon Jul 30 2018 Christian Lindig <christian.lindig@citrix.com> - 2.19.0_sxm2-1
- Update list_changed_blocks docs

* Tue Jul 03 2018 Christian Lindig <christian.lindig@citrix.com> - 1.19.0_sxm2-1
- Upload docs from master branch

* Thu Jun 28 2018 Christian Lindig <christian.lindig@citrix.com> - 0.19.0_sxm2-1
- merge of GFS2 feature

* Thu May 24 2018 Christian Lindig <christian.lindig@citrix.com> - 0.17.0-1
- CA-289145: Close socket if error occurs when connecting

* Mon Apr 09 2018 Christian Lindig <christian.lindig@citrix.com> - 0.16.0-1
- CA-283254: formatting strings with % and .format differ in their handling of 
  unicode, with format being better.

* Wed Apr 04 2018 Marcello Seri <marcello.seri@citrix.com> - 0.15.0-2
- Update SPEC file to get rid of rpmbuild warnings

* Wed Apr 04 2018 Christian Lindig <christian.lindig@citrix.com> - 0.15.0-1
- CP-25274: SMAPIv3 interface change - Drop URI and use configuration instead
- CP-25274: SMAPIv3 interface change - Rework SR.probe return values
- CP-25274: Mark SR.probe()[0].sr as optional
- Make generated python classes modern subclasses of object
- Treat missing fields in struct as None
- A complete probe result can be used for SR.attach too

* Mon Mar 05 2018 Christian Lindig <christian.lindig@citrix.com> - 0.14.0-1
- Fix gh-pages generation
- OUnit 1's exitcode is broken, use OUnit2
- Fix tests after the introduction of the sharable flag
- .travis.yml: use opam env for generating gh pages
- generator/html: fix ocaml code example syntax highlight

* Wed Feb 28 2018 Christian Lindig <christian.lindig@citrix.com> - 0.13.0-1
- CA-283728: put generated code into new namespace
- CA-283728: ship old version of SMAPIv3 generated code for 
- Move lost __init__.py patch from spec file to repository
  compatibility with old tmpfsSR
- Fix some flake8 warnings in the generated code

* Fri Feb 23 2018 Edwin Török <edvin.torok@citrix.com> - 0.12.0-2
- Move lost __init__.py patch from spec to repository
- CA-283728: ship old version of SMAPIv3 generated code for compatibility with pvsproxy

* Thu Feb 22 2018 Christian Lindig <christian.lindig@citrix.com> - 0.12.0-1
- Remove redundant definition of function pipe (|>)
- Update issue link to xapi-project repo

* Fri Feb 09 2018 Christian Lindig <christian.lindig@citrix.com> - 0.11.0-1
- Add uuid to SR.create call and return a URI
- CP-24350: plumb through sharable flag
- CA-273748: Support boolean positional arguments in python autogen CLI
- CA-272163: add new exception for redirection
- CA-272163: do not loose exception type during RPC
- CA-277837: SR.attach: take a uuid parameter too
- generator: fix warnings (including ambiguous doc comments)

* Tue Jan 30 2018 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 0.10.0-1
- CP-26711: Ported build from oasis to jbuilder.

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 0.9.0-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Thu Mar  2 2017 Gabor Igloi <gabor.igloi@citrix.com> - 0.9.0-1
- Depend on xs-opam-repo providing updated OCaml libraries:
  Port to new rpc and cow libraries.

* Tue Feb 28 2017 Christian Lindig <christian.lindig@citrix.com> - 0.8.3-1
- Upgrade to Foundation 6.2.1 for the HTML framework

* Mon Mar 21 2016 Euan Harris <euan.harris@citrix.com> - 0.8.2-2
- Move OCaml plugin libraries into a subcomponent

* Mon Oct 5 2015 Robert Breker <robert.breker@citrix.com> - 0.8.2-1
- Update to 0.8.2

* Tue Sep 29 2015 Robert Breker <robert.breker@citrix.com> - 0.8.1-1
- Update to 0.8.1

* Fri Sep 11 2015 David Scott <dave.scott@citrix.com> - 0.8-3
- Update to 0.8

* Wed Sep  9 2015 David Scott <dave.scott@citrix.com> - 0.7-1
- Update to 0.7

* Tue Aug  4 2015 David Scott <dave.scott@citrix.com> - 0.6-1
- Update to 0.6

* Wed Jul 15 2015 David Scott <dave.scott@citrix.com> - 0.5-1
- Update to 0.5

* Wed Jul 8 2015 David Scott <dave.scott@citrix.com> - 0.4-2
- Update to 0.4

* Tue Jul 7 2015 David Scott <dave.scott@citrix.com> - 0.3-1
- Update to 0.3

* Mon Apr 27 2015 David Scott <dave.scott@citrix.com> - 0.2.1-1
- Update to 0.2.1

* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 0.1.1-1
- Update to 0.1.1

* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
