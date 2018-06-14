"""Util methods for Waffle checks"""

from cms.djangoapps.contentstore.config.waffle import waffle, ENABLE_COURSE_HEALTH_PAGE, ENABLE_COURSE_HEALTH_QUALITY
# from courseware.access import has_access
from student.roles import GlobalStaff


def should_show_course_health_page(requesting_user):
  """
    Determine if the COURSE_HEALTH_PAGE waffle is set
    and if the user is able to see it
  """

  if waffle().is_enabled(ENABLE_COURSE_HEALTH_PAGE):
    if GlobalStaff().has_user(requesting_user):
      return True

  return False

def should_show_course_health_quality(requesting_user, course_key):
  """
    Determine if the COURSE_HEALTH_PAGE waffle is set
    and if the user is able to see it
  """

  if ENABLE_COURSE_HEALTH_QUALITY.is_enabled(course_key):
    if GlobalStaff().has_user(requesting_user):
      return True

  return False
