from src.repositories.organizationRepository import OrganizationRepository
from api.liveGolfData import LiveGolfData
from src.module.organization import Organization


class OrganizationService:
    def __init__(self):
        self.repo = OrganizationRepository()
        self.api = LiveGolfData()

    def _refresh_organizations(self):
        # Call API to fetch live data
        org_data = self.api.get_organizations()

        # Clear existing and refresh
        self.repo.delete_all_organizations()
        orgs = []
        for o in org_data:
            org = Organization(_name=o["orgName"], _external_id=o["orgId"])
            org.id = self.repo.insert_organization(org)
            orgs.append(org)

        return orgs

    def get_organizations(self, force_refresh=False):
        if force_refresh:
            print("Refreshing organizations due to user request.")
            return self._refresh_organizations()
        else:
            orgs = self.repo.get_organizations()
            if not orgs:
                orgs = self._refresh_organizations()
            return orgs
