import duckdb
from typing import List
from src.module.organization import Organization


class OrganizationRepository:
    """
    Repository for managing golf organizations in a DuckDB database.
    Attributes:
        conn (duckdb.DuckDBPyConnection): Connection to the DuckDB database.
    """

    def __init__(self, db_path="golf_pool.db"):
        self.conn = duckdb.connect(db_path)

    def get_organizations(self) -> List[Organization]:
        rel = self.conn.sql("SELECT * FROM organization")
        columns = rel.columns
        rows = rel.fetchall()

        results = [dict(zip(columns, row)) for row in rows]
        return [
            Organization(
                _id=row["id"], _name=row["name"], _external_id=row["external_id"]
            )
            for row in results
        ]

    def insert_organization(self, org: Organization) -> int:
        new_id = self.conn.execute(
            "INSERT INTO organization (name, external_id) VALUES (?, ?) RETURNING id",
            (org.name, org.external_id),
        ).fetchone()[0]
        return new_id

    def delete_all_organizations(self):
        self.conn.execute("DELETE FROM Organization")
