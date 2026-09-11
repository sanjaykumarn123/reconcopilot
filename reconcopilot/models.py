from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Target(Base):
    __tablename__ = "targets"
    id = Column(Integer, primary_key=True)
    program_name = Column(String, nullable=False)
    scope_notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    endpoints = relationship("Endpoint", back_populates="target")


class Endpoint(Base):
    __tablename__ = "endpoints"
    id = Column(Integer, primary_key=True)
    target_id = Column(Integer, ForeignKey("targets.id"))
    host = Column(String)
    url = Column(String, nullable=False)
    status_code = Column(Integer)
    title = Column(String)
    tech_stack = Column(String)
    source_tool = Column(String)          # subfinder / httpx / katana / nuclei / burp
    risk_score = Column(Integer)          # filled in by `score`
    ai_reasoning = Column(Text)
    suggested_vuln_class = Column(String)

    target = relationship("Target", back_populates="endpoints")
    findings = relationship("Finding", back_populates="endpoint")


class Finding(Base):
    __tablename__ = "findings"
    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, ForeignKey("endpoints.id"))
    notes = Column(Text)                  # your manual testing log
    confirmed = Column(Boolean, default=False)

    endpoint = relationship("Endpoint", back_populates="findings")
    reports = relationship("Report", back_populates="finding")


class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True)
    finding_id = Column(Integer, ForeignKey("findings.id"))
    markdown_content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    finding = relationship("Finding", back_populates="reports")