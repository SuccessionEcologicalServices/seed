# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-22 20:17
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


def forwards(apps, schema_editor):
    PropertyAuditLog = apps.get_model("seed", "PropertyAuditLog")
    TaxLotAuditLog = apps.get_model("seed", "TaxLotAuditLog")

    # delete some very specific *AuditLogs that were causing issues because they were one offs
    try:
        pal = PropertyAuditLog.objects.get(
            description='{"extra_data_fields": [], "regular_fields": ["city"]}')

        pal.delete()
    except PropertyAuditLog.DoesNotExist:
        pass

    try:
        pal = PropertyAuditLog.objects.get(
            description='Initial audit log added on update.')
        pal.delete()
    except PropertyAuditLog.DoesNotExist:
        pass

    try:
        tal = TaxLotAuditLog.objects.get(
            description='{"extra_data_fields": [], "regular_fields": ["city"]}')
        tal.delete()
    except TaxLotAuditLog.DoesNotExist:
        pass

    try:
        tal = TaxLotAuditLog.objects.get(
            description='Initial audit log added on update.')
        tal.delete()
    except TaxLotAuditLog.DoesNotExist:
        pass

    for p in PropertyAuditLog.objects.all():
        print "\n----PropertyAuditLog----"
        print "ID: {}   Description:  {}".format(p.pk, p.description)

        if not p.name:
            if p.description == 'Initial audit log added on creation/save.':
                p.name = 'Import Creation'

        # print "State: {}".format(p.state.pk)
        property_state_1 = None
        property_state_2 = None
        if p.parent1:
            # print "Parent State 1: {}".format(p.parent1.state)
            property_state_1 = p.parent1.state
        else:
            print "Parent 1 was None"
        if p.parent2:
            # print "Parent State 2: {}".format(p.parent2.state)
            property_state_2 = p.parent2.state
        else:
            print "Parent 2 was None"

        p.parent_state1 = property_state_1
        p.parent_state2 = property_state_2
        p.save()

    for t in TaxLotAuditLog.objects.all():
        print "\n----TaxLotAuditLog----"
        print "ID: {}   Description:  {}".format(t.pk, t.description)

        if not t.name:
            if t.description == 'Initial audit log added on creation/save.':
                t.name = 'Import Creation'

        # print "State: {}".format(p.state.pk)
        tax_lot_state_1 = None
        tax_lot_state_2 = None
        if t.parent1:
            # print "Parent State 1: {}".format(p.parent1.state)
            tax_lot_state_1 = t.parent1.state
        else:
            print "Parent 1 was None"
        if t.parent2:
            # print "Parent State 2: {}".format(p.parent2.state)
            tax_lot_state_2 = t.parent2.state
        else:
            print "Parent 2 was None"

        t.parent_state1 = tax_lot_state_1
        t.parent_state2 = tax_lot_state_2
        t.save()

    return

class Migration(migrations.Migration):
    dependencies = [
        ('seed', '0049_auto_20170222_1217'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]