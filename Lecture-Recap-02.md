
# Electric Sources
In the previous lecture we talked about the water pump as an equivalent for a voltage source but did not go into any details about it. It is now time to demystify electrical sources and to find out what they are. This will lay the gound work for future lectures and, more importantly, practical applications. But before we do that, let me exploit that water circulation equivalent for a little more.

## Counter Forces
Take a hand operated water pump for instance. It builds up pressure as long as I crank its handle. The harder I crank it, the more pressure I build up. And vice versa, the more pressure I want, the harder I have to turn. I will soon notice a counter force that puts a limit to my effords. (That limit is basically defined by my personal fitness level.) The counter force allways acts against me. If there was no counter force, I could create energy out of thin air! So if you drove a water wheel with my hand pump - like in our  first lecture's example - this counter force told you that you have to perform a certain amount of work. And that means spending energy - since we allways have to pay the piper! That is basically what the fundamental laws of thermodynamics state.

As a side note: in theory I don't have to spent energy just to building up pressure. Not until I move any water or even drive a water wheel with it. But the pump faces intrinsic friction losses, as does any electrical generator. Hence, this model is not so far from the thruth.

## Open Loop Voltage
<!-- Let us analyse what happens in the moment a water circuit is connected to a water pump. When the valve opens, the water will experience a relaxation and the pressure will slightly drop. You can imagin a standing crowd of people cramped together before the start of a demonstration. The crowd on the move is not as packed as the standing pulk of people. But let us assume the pump compensates for that. -->

Originally we were able to derive *Kirchhoff's Voltage Law* very nicely from a water model. The law states that the sum of all voltages in an (elctrical) circuit equals zero. Or put another way: The source voltage equals the sum of all (serial) voltage drops in the connected circuit. Applied to the circulation of water we can say: if we monitor the pressure at the pump and across the pipes, including any water wheel connected to them, we will be able to make this summation correctly in the same way at any time. 

### Can *Kirchhoff's Voltage Law (KVL) be violated?*
What conclusions can we make for the **static case**, when the valves of the pump are closed or when the source is disconnected from the load? In that case we can at least draw this parallel <!--Parallele ziehen-->: The pressure that builds up before any valves open for the water to flow, is equivalent to the voltage of any electrical source before its terminals are connected to a circuit. This is called the **Open Loop Voltage V<sub>o</sub>**. But what happens to the voltage or pressure drops of the circuit? It appears that the opposing pressure or voltage drops were missing - like there was a pump pressure or a source voltage only! What is left to sum up against V<sub>o</sub> like the *KVL* states? To anwer that, let us focus on voltages only for the moment.

### Closed Loops
Let us draw a voltage indicator in form of an arrow left to our source, from top to bottom. Let us name it **V<sub>s</sub>** for source voltage. And now we draw another indicator to the right of our source, from the top terminal to the bottom terminal or from plus to minus respectively. And we name it **V<sub>o</sub>** for it represents the open loop voltage. At first glance **V<sub>o</sub>** looks like the exact duplicate of **V<sub>s</sub>**.

Remember *Lecture #1* where we rearranged our arrows of source voltage and voltage drops? **V<sub>s</sub>** appeared to be in parallel to the sum of the Voltage drops along the wires and across the load resistor. But after a deft rearrangement we figured that the source voltage is **opposing** the other voltages but is equal in magnitude! The same rule applies here. **V<sub>s</sub>** and **V<sub>o</sub>** are just **vectors** in an **one-dimensional** space that is curved back into itself - in form of a **closed loop**, called a **circuit**. So mathematically we get **V<sub>s</sub>** = **V<sub>o</sub>** what can be rearranged to **V<sub>s</sub>** - **V<sub>o</sub>** = 0. This demonstrates that *KVL* is **not** violated. You cound simply imagine the open terminals as an infinite high resistance.

### Tighten the Grip
As always, I would like to take a more intuitive approach to completing this. Let's go back to our water circuit, which consists of a pump and a water wheel. Both are connected by two conduits. The water wheel sits so tightly in its housing, that no water can pass through unless it is turning. When the pump starts, water flows through the pipes and sets the water wheel in motion. Pressure drops occur along the pipes and accross the water wheel.

Now I grip the axle of the water wheel. The tighter I grip, the slower the water wheel becomes and the less water flows. As a consequence, the pressure drops in the conduits become smaller and smaller. But what happens to the pressure drop across the water wheel? Well *Kirchoff* gives the answer. If the pump maintains a constant pressure **p<sub>p</sub>**, the pressure drop **p<sub>w</sub>** at the wheel must increase as the pressure drop **p<sub>c</sub>** across the conduits goes down due to the reduced flow. Only then the equation p<sub>p</sub> = p<sub>c</sub> + p<sub>w</sub> holds true. When I stop the wheel, the flow stops and the pressure drops across the pipes vanish. Thus the pressure drop across the wheel **converges** with the pressure ceated by the pump. Therefore the **open circuit** is nothing other than the **limit transition** from the **dynamic** to the **static** case!

## The Chain of Cause and Effect
Let us now take a look at the chain of cause and effect and see where this takes us. I will use the water circuit and the electric circuit interchangeably and roll up the carpet of causality from the end.

Drops in pressure are either caused by friction in the pipes or by relaxation of the water as it passes trough the wheel. The water flow is caused by a pressure difference generated by the pump between its inlet and outlet connections. Further is the difference in pressure caused by the displacement of water molecules.

Let us now take a circuit consisting of a light bulb connected to a voltage source via two wires. Both the wires and the light bulb generate voltage drops caused by the current flowing through their ohmic resistances.
And the current flow is caused by the **difference in potential** generated by the voltage source.

Pay close attention to how we indicate the source voltage V<sub>s</sub>, the current I and the voltage drops V<sub>L</sub> in a circuit diagram. The arrow representing the source voltage points from the positive to the negative pole of the source - or from top to bottom. The current flows from the plus pole to the minus pole **through** the connected **circuit**. This means that the current flows from minus to plus **within** the voltage **source**! The arrow indicating the current flow is therefore pointing in the **opposite** direction of the **source** voltage. This is different from ohmic resistors, where the current arrow and the voltage arrow point in the same direction. And this is in accordance with *Kirchhoff's Voltage Law*, according to which the source and load voltages are directed in opposite directions.

## Separation of Charge
The only thing left in the causality chain of our electrical circuit is the propper equivalent for the displacement of the water molecules by the pump. When the pump is at rest, there is no pressure in the water circuit and no counterforce present to counteract the rotation of the pump. When the pump starts up, its rotation displaces the water molecules, which causes a pressure difference. And this is immediately noticeable through a counterforce. In the pump/pressure model we also can identify a source as a place where the flow is directed against the pressure drop. We could almost imagine the water flowing uphill. But there is no field involved.

In a pumped storage hydro power station on the other hand, water is pumped uphill against the gravitational field. This way electrical energy is converted to potential engery and stored. If electricity is needed, the water flows downhill and drives a turbine connected to an electrical generator. When the water is moved uphill, energy is spent. When it runs downhill, energy is gained, since energy can neither be generated nor destroyed.

How can all of this be applied to electrons? In fact, the electrons have to be moved against a certain field and this is the **electric field**! But in electricity things are fundamentally different. In the case of electrons we speak of **charge separation** instead of **displacement**. Let us assume that there is a phenomenon that separates these charges or electrons within a voltage source. Then they immediately experience a counterforce, just like the water molecules when the pump starts up. But it is very different in origin.

### Electrons in Wires
The moment we separate the electrons in our voltage source, an electric field appears at its terminals. But where does it emerge from? Charged particles, such as our negatively charged electrons, are **always** surrounded by an electric field that is directed radially outwards from the particle, just like light rays emanating from a light source.
*
In any electrical conductor, such as a copper wire, the electrons are already present and fill the space between the copper atoms. They can move relatively freely. As they are always surrounded by their own electric field, they influence each other due to the fact that every electron is always in the field of every other electron in its vicinity. Therefore, they spread evenly, almost like an electron gas, because particles with the same charge repel each other. But they will not perform any directed movement, **unless** we create an **imbalance** in their **spatial distribution**. And this is essentially what is meant by separation of charge.

### The Origin of Electric Current
As mentioned earlier,  we will observe an **outer** electric field that **counteracts** any **imbalance** we crerate and tries to distribute the electrons evenly again. But if we maintain that imbalance and connect an extermnal circuit, we crate a path for the electrons to escape from that area of increased charge density. The electric field will spread across the wires and drag the electrons towards the region of lower charge density which corresponds to the opposite pole of the voltage source. A current flows through our circuit!

## Methods of Charge Separation
<!--Gloss over briefly-->
But how can electric charges be seperatet after all? There are various physical effects that influcence electrons inside of a conductor and even in free space. I will gloss over the most common principals and give some examples of practical application, without going into details.

> * Induction (electric generator)
> * Photo-electric effect (solar panel)
> * Thermoelectric effect (temperature sensor, nuclear battery)
> * Electrochemical reactions (battery)

### Induction
Probably the most common way to generate electricity is the electric generator such as the bicycle dynamo. The underlying physical priciple is called induction. Inside any type of generator, there is a fundamental aspect of electromagnetism at work. Whenever a charged particle is exposed to a magnetic field, it experiences a force if it either **moves** relative to the magnetic field or the magnetic field **changes** in magnitude.

This can be accomplished in multiple ways. One of them is to rotate a coil of copper wire inside a constant magnetic field. The bicycle dynamo for instance has an inverse configuration: a permanent magnet revolves around a stationary coil.

### The Photo-electric Effect
[...]

### The Thermoelectric Effect
[...]

### Electric Battries
[...]

## Conclusion
<!--So inside a voltage source electrons are separated and moved against the electric field. One **difference** between pumping water uphill against the gravity field is, that they bring their **own** field with them. One **similarity** is that it **takes** energy to do it. Once done and a current flows through a circuit, the voltage source **provides** energy.-->

In a voltage source, the electrons are separated and moved against the electric field. One **difference** to water, which is pumped uphill against the gravitational field, is that the electrons bring their own field with them. One **similarity** is that energy is **required** for this. As soon as the electrons are constantly separated and a current flows through a circuit, the voltage source **supplies** electric energy to the circuit.

The **type** of energy it converts into electricity depends on which method of charge separation is used. The dynamo requires **mechanical** power, the solar panel needs **light** and the thermo element needs **heat**. The battery is a little different for it is electrically charged before it can deliver electricity. 

We can now even draw two **general** conclusions: Firstly, every energy source **takes** in and **delivers** energy at the same time. And secondly, the energy taken in is converted into the energy delivered. Every real energy **source** is therefore an energy **converter**.
