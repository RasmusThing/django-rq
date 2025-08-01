### Version 3.1 (2025-08-02)
* Added `/metrics` endpoint to expose RQ metrics in Prometheus format. Thanks @terencehonles!
* Added token based authentication for the `/metrics` and `/stats.json` endpoints. Thanks @RasmusThing!
* Migrated Django-RQ to use Python's modern packaging standard. Thanks @terencehonles!
* Fixed an issue with setting `result_ttl` via job decorators. Thanks @Sir-heed!
* Various admin page improvements. Thanks @selwin and @DhavalGojiya!

### Version 3.0.1 (2025-04-28)
* Temporarily disable `object-tools` block from job detail view. Thanks @terencehonles!
* Fixed a typo in `setup.py`. Thanks @terencehonles!
* Added support for RQ >= 2.2. Thanks @terencehonles!
* Properly handle cases where no `HOST` is specified in Redis config. Thanks @spapas!

### Version 3.0 (2024-10-28)
* Added support for RQ 2.0. Thanks @selwin!
* Many typing improvements. Thanks @SpecLad and @terencehonles!
* Added management command to suspend and resume workers. Thanks @jackkinsella!
* Better support for Redis Sentinel. Thanks @alaouimehdi1995!

### Version 2.10.2 (2024-03-23)
* Added support for Django 5.0. Thanks @selwin!
* Fixed an error in Python 3.12. Thanks @selwin!
* Fixes an issue that may happen if Redis port is not specified. Thanks @terencehonles!

### Version 2.10.1 (2023-12-18)
* Fixed packaging issues with 2.10.0.

### Version 2.10.0 (2023-12-18)
* Added `rqworker-pool` management command. Thanks @chromium7!
* Compatibility with Django 5.0. Thanks @perry!
* The scheduler now defaults to db 0. Thanks @bennylope!

### Version 2.9.0 (2023-11-26)
* Added an option to delete all failed jobs. Thanks @chromium7!
* You can now specify `SERIALIZER` option while declaring queues in `settings.py` Thanks @sophcass!
* Updated templates to match newer versions of Django admin's styling. Thanks @nikhilweee!
* Don't show `Empty Queue` button on registry pages. Thanks @selwin!

### Version 2.8.1 (2023-05-14)
* Added a button to stop currently running jobs. Thanks @gabriels1234!
* Added a failed jobs column to rqstats command. Thanks @dangquangdon!
* Explicitly requires RQ >= 1.14 in `setup.py`. Thanks @selwin!

### Version 2.8.0 (2023-05-02)
* Support for RQ 1.14. Thanks @Cerebro92 and @selwin!
* Show scheduler PID information in admin interface. Thanks @gabriels1234!
* Added `serializer` argument to `rqworker` command. Thanks @gabriels1234!
* Added `USERNAME` and `SENTINEL_KWARGS` support. Thanks @joachimBurket!

### Version 2.7.0 (2023-02-07)
* Able to show multiple execution results for each job (requires RQ v1.12). Thanks @selwin!
* Various admin interface improvements. Thanks @selwin!

### Version 2.6.0 (2022-11-05)
* Added `--max-jobs` argument to `rqworker` management command. Thanks @arpit-goel!
* Remove job from `ScheduledJobRegistry` if a scheduled job is enqueued from admin. Thanks @robertaistleitner!
* Minor code cleanup. Thanks @reybog90!

### Version 2.5.1 (2021-11-22)
* `Redis.from_url` does not accept `ssl_cert_reqs` argument for non SSL Redis URL. Thanks @barash-asenov!

### Version 2.5.0 (2021-11-17)
* Better integration with Django admin, along with a new `Access admin page` permission that you can selectively grant to users. Thanks @haakenlid!
* Worker count is now updated everytime you view workers for that specific queue. Thanks @cgl!
* Add the capability to pass arbitrary Redis client kwargs. Thanks @juanjgarcia!
* Always escape text when rendering job arguments. Thanks @rhenanbartels!
* Add `@never_cache` decorator to all Django-RQ views. Thanks @Cybernisk!
* `SSL_CERT_REQS` argument should also be passed to Redis client even when Redis URL is used. Thanks @paltman!

### Version 2.4.1 (2021-03-31)
* Added `ssl_cert_reqs` and `username` to queue config. Thanks @jeyang!

### Version 2.4.0 (2020-11-08)
* Various admin interface improvements. Thanks @selwin and @atten!
* Improved Sentry integration. Thanks @hugorodgerbrown and @kichawa!

### Version 2.3.2 (2020-05-13)
* Compatibility with RQ >= 1.4.0 which implements customizable serialization method. Thanks @selwin!

### Version 2.3.1 (2020-04-10)
* Added `--with-scheduler` argument to `rqworker` management command. Thanks @stlk!
* Fixed a bug where opening job detail would crash if job.dependency no longer exists. Thanks @selwin!

### Version 2.3.0 (2020-02-09)
* Support for RQ's new `ScheduledJobRegistry`. Thanks @Yolley!
* Improve performance when displaying pages showing a large number of jobs by using `Job.fetch_many()`. Thanks @selwin!
* `django-rq` will now automatically cleanup orphaned worker keys in job registries. Thanks @selwin!
* Site name now properly displayed in Django-RQ admin pages. Thanks @tom-price!
* `NoSuchJobError`s are now handled properly when requeuing all jobs. Thanks @thomasmatecki!
* Support for displaying jobs with names containing `$`. Thanks @gowthamk63!

### Version 2.2.0 (2019-12-08)
- Support for Django 3.0. This release also drops support for Django 1.X. Thanks @hugorodgerbrown!
- `rqworker` management command now properly passes in `--verbosity` to `Worker`. Thanks @stlk!
- The admin interface can now view jobs with `:` on their IDs. Thanks @carboncoop!
- Job detail page now shows `job.dependency`. Thanks @selwin!

### Version 2.1.0 (2019-06-14)
- Fixed `Requeue All`
- Django-RQ now automatically runs maintenance tasks when `rq_home` is opened

### Version 2.0 (2019-04-06)
- Compatibility with RQ 1.0 (Thanks @selwin). Backward incompatible changes include:
  * `FailedQueue` is now replaced by `FailedJobRegistry`
  * RQ now uses `sentry-sdk` to send job failures to Sentry.
- Scheduler now respects default `timeout` and `result_ttl` defined in `RQ_QUEUES`. Thanks @simone6021!
- Minor improvements and bug fixes. Thanks @selwin!


### Version 1.3.1 (2019-03-15)
- Run `rqworker` with `--sentry_dsn=""` to disable Sentry integration. Thanks @Bolayniuss!
- Support for `SSL` Redis kwarg. Thanks @ajknv!
- `rqworker`and `rqscheduler` management commands now uses RQ's built in `setup_loghandlers` function. Thanks @Paulius-Maruska!
- Remove the use of deprecated `admin_static` template tag. Thanks @lorenzomorandini!


### Version 1.3.0 (2018-12-18)
- Added support `redis-py` >= 3 and `RQ` >= 0.13. Thanks @selwin!
- Use `Worker.count(queue=queue)` to speed up the process of getting the number of active workers. Thanks @selwin!
- Added an option to requeue job from the admin interface. Thanks @seiryuz!
- Improve Sentinel support. Thanks @pnuckowski!


### Version 1.2.0 (2018-07-26)
- Supports Python 3.7 by renaming `async` to `is_async`. Thanks @Flimm!
- `UnpickleError` is now handled properly. Thanks @selwin!
- Redis Sentinel support. Thanks @SpeedyCoder!


### Version 1.1.0
- Fixed some admin related bugs. Thanks @seiryuz!
- More Django 2.0 compatibility fixes. Thanks @selwin and @koddr!
- Custom `Job` and `Worker` classes are now supported. Thanks @skirsdeda!
- `SENTRY_DSN` value in `settings.py` will now be used by default. Thanks @inetss!


### 1.0.1
- Django 2.0 compatibility fixes.
- Minor bug fixes


### 1.0.0

-   You can now view worker information
-   Detailed worker statistics such as failed/completed job count are
    now shown (requires RQ &gt;= 0.9.0). Thanks @seiryuz!
-   `rqstats` management command now allows you to monitor queue stats
    via CLI. Thanks @seiryuz!
-   Added `/stats.json` endpoint to fetch RQ stats in JSON format,
    useful for monitoring purposes. Thanks @seiryuz!
-   Fixed a crash when displaying deferring jobs. Thanks @Hovercross!
-   Added `sentry-dsn` cli option to `rqworker` management command.
    Thanks @efi-mk!
-   Improved performance when requeueing all jobs. Thanks
    @therefromhere!

### 0.9.6

-   More Django 1.10 compatibility fixes. Thanks @dmwyatt!
-   Improves performance when dealing with a large number of workers.
    Thanks @lucastamoios!

### 0.9.5

-   Fixed view paging for registry-based job lists. Thanks @smaccona!
-   Fixed an issue where multiple failed queues may appear for the same
    connection. Thanks @depaolim!
-   `rqworker` management command now closes all DB connections before
    executing jobs. Thanks @depaolim!
-   Fixed an argument parsing bug `rqworker` management command. Thanks
    @hendi!

### 0.9.3

-   Added a `--pid` option to `rqscheduler` management command. Thanks
    @vindemasi!
-   Added `--queues` option to `rqworker` management command. Thanks
    @gasket!
-   Job results are now shown on admin page. Thanks @mojeto!
-   Fixed a bug in interpreting `--burst` argument in `rqworker`
    management command. Thanks @claudep!
-   Added Requeue All feature in Failed Queue's admin page. Thanks
    @lucashowell!
-   Admin interface now shows time in local timezone. Thanks
    @randomguy91!
-   Other minor fixes by @jeromer and @sbussetti.

### 0.9.2

-   Support for Django 1.10. Thanks @jtburchfield!
-   Added `--queue-class` option to `rqworker` management command.
    Thanks @Krukov!

### 0.9.1

-   Added `-i` and `--queue` options to rqscheduler management command.
    Thanks @mbodock and @sbussetti!
-   Added `--pid` option to `rqworker` management command. Thanks
    @ydaniv!
-   Admin interface fixes for Django 1.9. Thanks @philippbosch!
-   Compatibility fix for `django-redis-cache`. Thanks @scream4ik!
-   *Backwards incompatible*: Exception handlers are now defined via
    `RQ_EXCEPTION_HANDLERS` in `settings.py`. Thanks @sbussetti!
-   Queues in django-admin are now sorted by name. Thanks @pnuckowski!

### 0.9.0

-   Support for Django 1.9. Thanks @aaugustin and @viaregio!
-   `rqworker` management command now accepts `--worker-ttl` argument.
    Thanks pnuckowski!
-   You can now easily specify custom `EXCEPTION_HANDLERS` in
    `settings.py`. Thanks @xuhcc!
-   `django-rq` now requires RQ &gt;= 0.5.5

### 0.8.0

-   You can now view deferred, finished and currently active jobs from
    admin interface.
-   Better support for Django 1.8. Thanks @epicserve and @seiryuz!
-   Requires RQ &gt;= 0.5.
-   You can now use StrictRedis with Django-RQ. Thanks @wastrachan!

### 0.7.0

-   Added `rqenqueue` management command for easy scheduling of tasks
    (e.g via cron
