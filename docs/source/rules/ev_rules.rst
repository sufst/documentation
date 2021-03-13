.. _EV:

EV - Electric Vehicles
======================

.. todo - add relevant section of pdf as downloadable file

.. todo - add all rules as sections

.. _EV1:

EV 1 - Definitions
------------------

.. _EV1.1:

EV 1.1 - Tractive System (TS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _EV1.1.1:

EV 1.1.1
    Tractive System (TS) – every part that is electrically connected to the motor(s) and TS accumulators.

.. _EV1.2:

EV 1.2 - Electric
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _EV1.2.1:

EV 1.2.1
    Galvanic Isolation – two electric circuits are defined as galvanically isolated, if all of the following are true:
        - the resistance between both circuits is ≥500 Ω/V, related to the maximum TS voltage of the vehicle, at a test voltage of maximum TS voltage or 250 V, whichever is higher.
        - the withstand voltage between both circuits is higher than three times the maximum TS voltage or 750 V, whichever is higher.

.. _EV2:

EV 2 - Electric Powertrain
--------------------------

.. _EV2.1:

EV 2.1 - Motors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _EV2.1.1:

EV 2.1.1
    Only electric motors are allowed.

.. _EV2.1.2:

EV 2.1.2
    Motor attachments must follow :ref:`T10 <T10>`
    
.. _EV2.1.3: 

EV 2.1.3
    Motor casings must follow :ref:`T7.3 <T7.3>`

.. _EV2.1.4: 

EV 2.1.4
    The motor(s) must be connected to the accumulator through a motor controller.

.. _EV2.2:

EV 2.2 - Power Limitation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _EV2.2.1:

EV 2.2.1
    The TS power at the outlet of the TS accumulator container must not exceed 80 kW.

.. _EV2.2.2:

EV 2.2.2
    Regenerating energy is allowed and unrestricted.

.. _EV2.2.3:

EV 2.2.3
    Wheels must not be spun in reverse.

.. _EV2.3:

EV 2.3 - APPS / Brake Pedal Plausibility Check
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _EV2.3.1:

.. _EV2.3.2:

.. _EV3:

EV 3 - General Requirements
---------------------------

.. _EV4:

EV 4 - Tractive System (TS)
---------------------------

.. _EV4.10:

EV 4.10 - Tractive System Active Light (TSAL)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _EV4.10.1:

EV 4.10.1
    The vehicles must include a single TSAL that must indicate the TS status. 
    The TSAL must not perform any other functions. 
    A TSAL with multiple LEDs in one housing is allowed.

.. _EV4.10.2:

EV 4.10.2
    The TS is active when ANY of the following conditions are true:
        - An accumulator isolation relay is closed.
        - The pre-charge relay, see EV5.7.2_, is closed.
        - The voltage outside the accumulator container(s) exceeds 60 VDC or 25 VAC Root Mean Square (RMS).

.. _EV4.10.3:

EV 4.10.3
    The TS is deactivated when ALL of the following conditions are true:
        - All accumulator isolation relays are opened.
        - The pre-charge relay, see EV5.7.2_, is opened.
        - The voltage outside the accumulator container(s) does not exceed 60 VDC or 25 VAC RMS.

.. _EV4.10.4:

EV 4.10.4
    The mentioned states of the relays (opened/closed) are the actual mechanical states. 
    The mechanical state can differ from the intentional state, i.e. if a relay is stuck. 
    Any circuitry detecting the mechanical state must meet EV5.6.2_.

.. _EV4.10.5:

EV 4.10.5
    The TSAL itself must:
        - Be red in color and flash continuously with a frequency between 2 Hz and 5 Hz if and only if the TS is active, see EV4.10.2_, and the LVS is switched on.
        - Be green in color and continuously illuminated if and only if the TS is deactivated, see EV4.10.3_, and the LVS is switched on.
    
.. _EV4.10.6:

EV 4.10.6
    The TSAL must:
        - Be located lower than the highest point of the main hoop and including the mounting within the rollover protection envelope, see :ref:`T1.1.14 <T1.1.14>`.
        - Be no lower than 150 mm from the highest point of the main hoop.
        - Not be able to contact the driver’s helmet in any circumstances.

.. _EV4.10.7:

EV 4.10.7
    The entire illuminated surface of the TSAL must be clearly visible:
        - Except for small angles which are blocked by the main hoop.
        - From a point 1.60 m vertically from ground level, within 3 m horizontal radius from the TSAL.
        - In direct sunlight.

.. _EV4.10.8:

EV 4.10.8
    The TSAL and all needed circuitry must be hard wired electronics. Software control is not permitted.

.. _EV4.10.9:

EV 4.10.9
    A green indicator light in the cockpit that is easily visible even in bright sunlight and clearly marked with “TS off” must light up if the TS is deactivated, see EV4.10.3_.

.. _EV4.10.10:

EV 4.10.10
    Signals influencing the TSAL and the indicator according to EV4.10.9_ are SCS, see :ref:`T11.9 <T11.9>`.
    The safe state for the TSAL is defined as TSAL non-illuminated. 
    The TSAL has an active indication of absence of failures (continuous green illumination) and thus must not be illuminated for visible check, see T11.9.5.

.. _EV4.10.11:

EV 4.10.11
    The TSAL must be designed, that a single point of failure within the TSAL circuitry will not show an activated TS as deactivated TS according to EV4.10.5_

.. _EV4.10.12:

EV 4.10.12
    The circuitry detecting the relay conditions mentioned in EV4.10.2_ and EV4.10.3_ does not need to detect an open circuit when the intentional state of the relay is opened. 
    The voltage detection circuit does not need to detect an open circuit if no voltage is present.

.. _EV4.10.13:

EV 4.10.13
    The voltage outside of the TS accumulator must at least be measured independently
        - accross DC-link capacitors in each housing with DC-link capacitors
        - at the vehicle side of the Accumulator Isolation Relays (AIRs) inside the accumulator container
    
    If there is any implausibility between the independent voltage measurements, the safe state must be entered regardless of the relay states.

.. _EV4.10.14:

EV 4.10.14
    If an TS accumulator container is removed from the vehicle, a device must be used which logically replaces the TSAL parts inside the accumulator container. 
    It must not be mechanically possible to electrically connect the TS accumulator container to the vehicle when this device is in place.

.. _EV5:

EV 5 - Tractive System Energy Storage
-------------------------------------

.. _EV5.6:

EV 5.6 - Accumulator Isolation Relays (AIRs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _EV5.6.1:

EV 5.6.1
    At least two AIRs must be fitted inside each TS accumulator container.

.. _EV5.6.2:

EV 5.6.2
    The AIRs must open both poles of the TS accumulator. 
    If the AIRs are open, no TS voltage may be present outside of the accumulator container and the vehicle side of the AIRs must be galvanically isolated from the accumulator side, see EV1.2.1_.

.. _EV5.6.2.3:

EV 5.6.3
    The AIRs must be mechanical relays of a “normally open” type. 
    Solid-state relays are prohibited.

.. _EV5.6.4:

EV 5.6.4
    The fuse protecting the accumulator TS circuit must have a rating lower than the maximum switch off current of the AIRs.

.. _EV5.7:

EV 5.7 - Pre-Charge Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _EV5.7.1:

EV 5.7.1
    A circuit that ensures that the intermediate circuit is pre-charged to at least 95 % of the actual TS accumulator voltage before closing the second AIR must be implemented. 
    Therefore the intermediate circuit voltage must be measured.

.. _EV5.7.2:

EV 5.7.2
    The pre-charge circuit must use a mechanical, normally open type relay. 
    All pre-charge current must pass through this relay.


.. _EV6:

EV 6 - General Requirements
---------------------------

.. _EV7:

EV 7 - General Requirements
---------------------------

.. _EV8:

EV 8 - General Requirements
---------------------------

.. _EV9:

EV 9 - General Requirements
---------------------------