from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^explore/$',
        view=views.ExploreUsers.as_view(),
        name='explore_users'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_users'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='unfollow_users'
    ),
    url(
        regex=r'^(?P<username>\w+)/followers/$',
        view=views.userFollowers.as_view(),
        name='user_followers'
    ),
    url(
        regex=r'^(?P<username>\w+)/following/$',
        view=views.userFollowing.as_view(),
        name='user_following'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search'
    ),
     url(
        regex=r'^(?P<username>\w+)/$',
        view=views.UserProfile.as_view(),
        name='user_profile'
    ),
]
