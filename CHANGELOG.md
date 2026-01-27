# Changelog

## 0.1.0-alpha.2 (2026-01-27)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/stiggio/stigg-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** api update ([cb4996d](https://github.com/stiggio/stigg-python/commit/cb4996da81403af3f049d0c70d12ca7ce7cc3520))
* **api:** api update ([7706756](https://github.com/stiggio/stigg-python/commit/7706756ba1926cfddcdd54223197d9c49b2ea458))
* **api:** api update ([e8a240b](https://github.com/stiggio/stigg-python/commit/e8a240b5194b9a8c98ed72e3adaa5fddc814b8e4))
* **api:** comment out promotional endpoints ([60e1e7c](https://github.com/stiggio/stigg-python/commit/60e1e7c9cf3010ea1e239f51ff17c100c5c332db))
* **api:** improved cursor pagination ([cb953cc](https://github.com/stiggio/stigg-python/commit/cb953cc0a7530b5383bab867c4ad6936894901bd))

## 0.1.0-alpha.1 (2026-01-26)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/stiggio/stigg-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** added customer endpoints ([ca52e6d](https://github.com/stiggio/stigg-python/commit/ca52e6d8e130927932e8e0cacf646ca8e41078e7))
* **api:** api update ([2384ea5](https://github.com/stiggio/stigg-python/commit/2384ea56247be33f5d481335e3dd9a06f742a129))
* **api:** api update ([d262e32](https://github.com/stiggio/stigg-python/commit/d262e32f4171b373e7507e42c2f0e5d630a8ce41))
* **api:** api update ([2ff9ff9](https://github.com/stiggio/stigg-python/commit/2ff9ff922ff914369e66dfed4e90e3f7633f6a39))
* **api:** manual updates ([33e6ab1](https://github.com/stiggio/stigg-python/commit/33e6ab1119310d8ea5e0ce7018c495d0b201b072))
* **api:** manual updates ([408c84e](https://github.com/stiggio/stigg-python/commit/408c84e3a4e0857f46af8e2218f4a1737bcaa29c))
* **api:** manual updates ([e55bcad](https://github.com/stiggio/stigg-python/commit/e55bcad977fa9fa57cf6b9de0af2cce9f9da646e))
* **api:** manual updates ([7bcf910](https://github.com/stiggio/stigg-python/commit/7bcf910f7bb1750b299178f7a59839b56cfa20c7))
* **api:** update via SDK Studio ([5617c39](https://github.com/stiggio/stigg-python/commit/5617c39c42fbb57e492a3f020a284b6f7e9f7216))
* **api:** update via SDK Studio ([97e4313](https://github.com/stiggio/stigg-python/commit/97e43131abe401eeae8378787db8b33b845a4f70))
* **api:** update via SDK Studio ([b54e88a](https://github.com/stiggio/stigg-python/commit/b54e88a8e2f17d0c2945107ebdb3301e5f10a169))
* clean up environment call outs ([9569626](https://github.com/stiggio/stigg-python/commit/9569626237d0ed6a35dca344520217257abb080e))
* **client:** add support for binary request streaming ([ab062e0](https://github.com/stiggio/stigg-python/commit/ab062e027351c58c3ac30aa6e681de14208d59e9))
* **client:** support file upload requests ([1f6e2ed](https://github.com/stiggio/stigg-python/commit/1f6e2ed3579a2e5e36871ab121a6b7125558216a))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([9e80b71](https://github.com/stiggio/stigg-python/commit/9e80b711f0db270a0cabddc37642f2863e66ea9b))
* compat with Python 3.14 ([20c4f4c](https://github.com/stiggio/stigg-python/commit/20c4f4c7bb67ab2664f1ea96d5081a998a312732))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([6483a54](https://github.com/stiggio/stigg-python/commit/6483a54b976b4838881e4e461762c9170590f073))
* ensure streams are always closed ([cd64484](https://github.com/stiggio/stigg-python/commit/cd6448493343bbc95ae9802de7a998ebd2fa6921))
* **parsing:** correctly handle nested discriminated unions ([17587f2](https://github.com/stiggio/stigg-python/commit/17587f2501f8769956012fe7d5b3c36b08dc21dc))
* **parsing:** ignore empty metadata ([cce02c3](https://github.com/stiggio/stigg-python/commit/cce02c3acfcf557d7a5406d9218cbd6f15e39102))
* **parsing:** parse extra field types ([aa74584](https://github.com/stiggio/stigg-python/commit/aa7458479e955d35ecff1374a3cdb3fe538cba2a))
* use async_to_httpx_files in patch method ([a965ff1](https://github.com/stiggio/stigg-python/commit/a965ff1d0bcbc731fcf16f49e61f0273985d20a7))


### Chores

* add Python 3.14 classifier and testing ([08d8682](https://github.com/stiggio/stigg-python/commit/08d868213fa00ab27258a40f49ef66f47bd3b9d0))
* **ci:** upgrade `actions/github-script` ([7902494](https://github.com/stiggio/stigg-python/commit/79024947fa7a3febbb847f70bbaf771c7148f128))
* configure new SDK language ([e27d809](https://github.com/stiggio/stigg-python/commit/e27d80998d6471c0750cfe431f34bb88764493c2))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([b0da9be](https://github.com/stiggio/stigg-python/commit/b0da9befe88822c362aecc56be48c995a0493eca))
* **internal/tests:** avoid race condition with implicit client cleanup ([bcd2194](https://github.com/stiggio/stigg-python/commit/bcd2194d1746812841fad2184183dfdac09c55f8))
* **internal:** add `--fix` argument to lint script ([22d02dd](https://github.com/stiggio/stigg-python/commit/22d02dd493c319f882854d329d0f0c0fcd9da50e))
* **internal:** add missing files argument to base client ([fd30d29](https://github.com/stiggio/stigg-python/commit/fd30d2922734c52ccccc92bd97a76b7428a050f2))
* **internal:** bump pinned h11 dep ([68bbfb1](https://github.com/stiggio/stigg-python/commit/68bbfb177bebf495de82ba116bb2983a4d52644c))
* **internal:** codegen related update ([661eafb](https://github.com/stiggio/stigg-python/commit/661eafbf676a9ab947d59d94430643c74bebb4d4))
* **internal:** codegen related update ([0b6a4c2](https://github.com/stiggio/stigg-python/commit/0b6a4c2f9bb08639653069a2a6370d4eba1bc48f))
* **internal:** fix ruff target version ([5c10751](https://github.com/stiggio/stigg-python/commit/5c10751f1815d41f9910e8b19d83bd64ee24a893))
* **internal:** grammar fix (it's -&gt; its) ([7d3a5b4](https://github.com/stiggio/stigg-python/commit/7d3a5b4a66cbfb97fd50a11f4c9edb12b81fcce0))
* **internal:** update `actions/checkout` version ([160fe5d](https://github.com/stiggio/stigg-python/commit/160fe5d9898e553afb0663e0947206b580570038))
* **internal:** update comment in script ([cb98268](https://github.com/stiggio/stigg-python/commit/cb982683eef08d89a74f3662ec64ebee7e967545))
* **package:** drop Python 3.8 support ([0ff6c51](https://github.com/stiggio/stigg-python/commit/0ff6c513884b26f7ce53f9c99a6e80aaee0efd9f))
* **package:** mark python 3.13 as supported ([072b841](https://github.com/stiggio/stigg-python/commit/072b8414da27724eca52a57ce1eb35a0b13f1b48))
* **project:** add settings file for vscode ([a4c8f17](https://github.com/stiggio/stigg-python/commit/a4c8f17dc31a4253e0e10379a71cbc07f288d50d))
* **readme:** fix version rendering on pypi ([8a8a08c](https://github.com/stiggio/stigg-python/commit/8a8a08c2c59e8fcb5d2948b591732a5196ff2c13))
* speedup initial import ([c047340](https://github.com/stiggio/stigg-python/commit/c047340c56c0303a0cb1fbc30fafaf6b2df1a000))
* update @stainless-api/prism-cli to v5.15.0 ([677f30d](https://github.com/stiggio/stigg-python/commit/677f30dfdd61668703ad529b7c7f8d8cd87b9eef))
* update SDK settings ([3d37414](https://github.com/stiggio/stigg-python/commit/3d374148654dec3c7bc0a49b21f9081a90c6a1dc))
* update SDK settings ([a71fc34](https://github.com/stiggio/stigg-python/commit/a71fc34532b125523aabcaa85b996005ac6bfe81))
