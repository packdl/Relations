register(REPORT,
    id   = 'Relations',
    name = _('Relations'),
    description = _("Produces a relationship report about two individuals "
                    "  "),
    version = '1.0',
    gramps_target_version = '4.1',
    status = STABLE,
    fname = 'Relations.py',
    authors = ["Derik Pack"],
    authors_email = ["bob@email.com"],
    category = CATEGORY_TEXT,
    reportclass = 'Relations',
    optionclass = 'RelationsOptions',
    report_modes = [REPORT_MODE_GUI],
    require_active = True
    )
