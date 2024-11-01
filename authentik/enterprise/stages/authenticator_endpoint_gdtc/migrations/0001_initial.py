# Generated by Django 5.0.9 on 2024-10-22 11:40

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authentik_flows", "0027_auto_20231028_1424"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthenticatorEndpointGDTCStage",
            fields=[
                (
                    "stage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_flows.stage",
                    ),
                ),
                ("friendly_name", models.TextField(null=True)),
                ("credentials", models.JSONField()),
                (
                    "configure_flow",
                    models.ForeignKey(
                        blank=True,
                        help_text="Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="authentik_flows.flow",
                    ),
                ),
            ],
            options={
                "verbose_name": "Endpoint Authenticator Google Device Trust Connector Stage",
                "verbose_name_plural": "Endpoint Authenticator Google Device Trust Connector Stages",
            },
            bases=("authentik_flows.stage", models.Model),
        ),
        migrations.CreateModel(
            name="EndpointDevice",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="The human-readable name of this device.", max_length=64
                    ),
                ),
                (
                    "confirmed",
                    models.BooleanField(default=True, help_text="Is this device ready for use?"),
                ),
                ("last_used", models.DateTimeField(null=True)),
                ("uuid", models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                (
                    "host_identifier",
                    models.TextField(
                        help_text="A unique identifier for the endpoint device, usually the device serial number",
                        unique=True,
                    ),
                ),
                ("data", models.JSONField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "Endpoint Device",
                "verbose_name_plural": "Endpoint Devices",
            },
        ),
        migrations.CreateModel(
            name="EndpointDeviceConnection",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("attributes", models.JSONField()),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authentik_stages_authenticator_endpoint_gdtc.endpointdevice",
                    ),
                ),
                (
                    "stage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authentik_stages_authenticator_endpoint_gdtc.authenticatorendpointgdtcstage",
                    ),
                ),
            ],
        ),
    ]
