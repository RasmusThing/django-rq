from django.urls import re_path

from . import stats_views, views
from .contrib.prometheus import RQCollector

metrics_view = [
    re_path(r'^metrics/?$', stats_views.prometheus_metrics, name='rq_metrics'),
] if RQCollector else []  # type: ignore[truthy-function]

urlpatterns = [
    re_path(r'^$', stats_views.stats, name='rq_home'),
    re_path(r'^stats.json/?$', stats_views.stats_json, name='rq_home_json'),
    re_path(r'^stats.json/(?P<token>[\w]+)?/?$', stats_views.stats_json, name='rq_home_json'),
    *metrics_view,
    re_path(r'^queues/(?P<queue_index>[\d]+)/$', views.jobs, name='rq_jobs'),
    re_path(r'^workers/(?P<queue_index>[\d]+)/$', views.workers, name='rq_workers'),
    re_path(r'^workers/(?P<queue_index>[\d]+)/(?P<key>[-\w\.\:\$]+)/$', views.worker_details, name='rq_worker_details'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/finished/$', views.finished_jobs, name='rq_finished_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/failed/$', views.failed_jobs, name='rq_failed_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/failed/clear/$', views.delete_failed_jobs, name='rq_delete_failed_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/scheduled/$', views.scheduled_jobs, name='rq_scheduled_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/started/$', views.started_jobs, name='rq_started_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/deferred/$', views.deferred_jobs, name='rq_deferred_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/empty/$', views.clear_queue, name='rq_clear'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/requeue-all/$', views.requeue_all, name='rq_requeue_all'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/(?P<job_id>[^/]+)/$', views.job_detail, name='rq_job_detail'),
    re_path(
        r'^queues/(?P<queue_index>[\d]+)/(?P<job_id>[^/]+)/delete/$', views.delete_job, name='rq_delete_job'
    ),
    re_path(r'^queues/confirm-action/(?P<queue_index>[\d]+)/$', views.confirm_action, name='rq_confirm_action'),
    re_path(r'^queues/actions/(?P<queue_index>[\d]+)/$', views.actions, name='rq_actions'),
    re_path(
        r'^queues/(?P<queue_index>[\d]+)/(?P<job_id>[^/]+)/requeue/$',
        views.requeue_job_view,
        name='rq_requeue_job',
    ),
    re_path(
        r'^queues/(?P<queue_index>[\d]+)/(?P<job_id>[^/]+)/enqueue/$', views.enqueue_job, name='rq_enqueue_job'
    ),
    re_path(
        r'^queues/(?P<queue_index>[\d]+)/(?P<job_id>[^/]+)/stop/$', views.stop_job, name='rq_stop_job'
    ),
    re_path(r'^schedulers/(?P<scheduler_index>[\d]+)/$', views.scheduler_jobs, name='rq_scheduler_jobs'),
]
