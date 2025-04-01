from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class EmployeeLevel(str, Enum):
    L1_EXEC = "L1"  # Executives
    L2_MANAGER = "L2"  # Managers
    L3_SENIOR = "L3"  # Senior Staff
    L4_MID = "L4"  # Mid-Level Staff
    L5_JUNIOR = "L5"  # Junior Staff & Interns


class Department(str, Enum):
    ENGINEERING = "engineering"
    PRODUCT = "product"
    HR = "hr"
    SALES = "sales"
    MARKETING = "marketing"
    OPERATIONS = "operations"


class WorkspaceType(str, Enum):
    PRIVATE_OFFICE = "private_office"
    MANAGERIAL_CABIN = "managerial_cabin"
    FIXED_WORKSTATION = "fixed_workstation"
    HOT_DESK = "hot_desk"
    MEETING_ROOM = "meeting_room"
    CONFERENCE_HALL = "conference_hall"
    COLLABORATION_SPACE = "collaboration_space"
    BREAKOUT_AREA = "breakout_area"


class Employee(BaseModel):
    id: str = Field(..., description="Unique employee identifier")
    name: str = Field(..., description="Employee's full name")
    level: EmployeeLevel = Field(..., description="Employee's hierarchical level")
    department: Department = Field(..., description="Employee's department")
    preferences: dict = Field(default_factory=dict, description="Workspace preferences")
    join_date: datetime = Field(..., description="Employee's joining date")
    workspace_history: List[str] = Field(
        default_factory=list, description="History of assigned workspace IDs"
    )


class Workspace(BaseModel):
    id: str = Field(..., description="Unique workspace identifier")
    type: WorkspaceType = Field(..., description="Type of workspace")
    capacity: int = Field(..., description="Maximum capacity of the workspace")
    floor: int = Field(..., description="Floor number where workspace is located")
    zone: str = Field(..., description="Zone identifier within the floor")
    facilities: List[str] = Field(default_factory=list, description="Available facilities")
    current_occupants: List[str] = Field(
        default_factory=list, description="List of current occupant IDs"
    )
    availability_schedule: dict = Field(
        default_factory=dict, description="Availability schedule"
    )
    status: str = Field(default="available", description="Current status of workspace")


class WorkspaceRequest(BaseModel):
    employee_id: str = Field(..., description="ID of requesting employee")
    workspace_type: WorkspaceType = Field(..., description="Requested workspace type")
    start_time: datetime = Field(..., description="Requested start time")
    end_time: Optional[datetime] = Field(None, description="Requested end time")
    priority: int = Field(default=0, description="Request priority (0-10)")
    preferences: dict = Field(default_factory=dict, description="Special requirements")


class AllocationScore(BaseModel):
    workspace_id: str = Field(..., description="Workspace identifier")
    score: float = Field(..., description="Allocation score")
    factors: dict = Field(..., description="Scoring factors breakdown")


class FeedbackMetrics(BaseModel):
    comfort: int = Field(..., ge=1, le=5, description="Comfort rating")
    accessibility: int = Field(..., ge=1, le=5, description="Accessibility rating")
    noise_level: int = Field(..., ge=1, le=5, description="Noise level rating")
    overall_satisfaction: int = Field(..., ge=1, le=5, description="Overall satisfaction")
    comments: Optional[str] = Field(None, description="Additional feedback comments")