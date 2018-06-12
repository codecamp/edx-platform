"""
This module contains various configuration settings via
waffle switches for the contentstore app.
"""
from openedx.core.djangoapps.waffle_utils import CourseWaffleFlag, WaffleFlagNamespace, WaffleSwitchNamespace

# Namespace
WAFFLE_NAMESPACE = u'studio'

# Switches
ENABLE_ACCESSIBILITY_POLICY_PAGE = u'enable_policy_page'
ENABLE_COURSE_HEALTH_PAGE = u'enable_course_health_page'


def waffle():
    """
    Returns the namespaced, cached, audited Waffle Switch class for Studio pages.
    """
    return WaffleSwitchNamespace(name=WAFFLE_NAMESPACE, log_prefix=u'Studio: ')


def waffle_flags():
    """
    Returns the namespaced, cached, audited Waffle Flag class for Studio pages.
    """
    return WaffleFlagNamespace(name=WAFFLE_NAMESPACE, log_prefix=u'Studio: ')


# Flags
ENABLE_IN_CONTEXT_IMAGE_SELECTION = CourseWaffleFlag(
    waffle_namespace=waffle_flags(),
    flag_name=u'enable_in_context_image_selection',
    flag_undefined_default=False
)

ENABLE_COURSE_HEALTH_QUALITY = CourseWaffleFlag(
    waffle_namespace=waffle_flags(),
    flag_name=u'enable_course_health_quality',
    flag_undefined_default=False
)
