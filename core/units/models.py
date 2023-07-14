from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic_tree.models import PolymorphicMPTTModel, PolymorphicTreeForeignKey


# A base model for the tree:

class BaseTreeNode(PolymorphicMPTTModel):
    parent = PolymorphicTreeForeignKey('self',
                                       blank=True,
                                       null=True,
                                       on_delete=models.CASCADE,
                                       related_name=
                                       'children',
                                       verbose_name=_('parent'))
    title = models.CharField(_("Title"), max_length=200)

    left_neighbor = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="left_neighbor_node",
        on_delete=models.SET_NULL,
        verbose_name=_("Left neighbor node"),
    )
    right_neighbor = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="right_neighbor_node",
        on_delete=models.SET_NULL,
        verbose_name=_("Right neighbor node"),
    )
    unit_name = models.CharField(max_length=30, null=True, blank=True)
    get_neighbors_data = models.BooleanField(default=False, verbose_name=_("Get neighbors data"))

    node_order_by = ["unit_name"]

    def __str__(self):
        return self.title

    class Meta(PolymorphicMPTTModel.Meta):
        verbose_name = _("Tree node")
        verbose_name_plural = _("Tree nodes")


class Units(BaseTreeNode):
    # opening_title = models.CharField(_("Opening title"), max_length=200)
    commander = models.ForeignKey(User, on_delete=models.CASCADE)
    subcommander = models.ManyToManyField(User, related_name="subcommanders")
    member = models.ManyToManyField(User, related_name="members")
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    acceptable_level_depth = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_("Access level")
    )
    accessible_units = models.TextField(null=True)
    # history = HistoricalRecords(bases=[UnitHistoryFieldsModel])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    # history = HistoricalRecords(m2m_fields=[sub_commanders], bases=[UnitHistoryFieldsModel])

    can_have_children = True

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")
