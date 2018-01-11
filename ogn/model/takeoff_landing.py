from sqlalchemy import Boolean, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class TakeoffLanding(Base):
    __tablename__ = 'takeoff_landings'

    id = Column(Integer, primary_key=True)

    is_takeoff = Column(Boolean)
    timestamp = Column(DateTime, index=True)
    track = Column(Integer)

    # Relations
    airport_id = Column(Integer, ForeignKey('airports.id', ondelete='SET NULL'), index=True)
    airport = relationship('Airport', foreign_keys=[airport_id], backref='takeoff_landings')

    device_id = Column(Integer, ForeignKey('devices.id', ondelete='SET NULL'), index=True)
    device = relationship('Device', foreign_keys=[device_id], backref='takeoff_landings')
