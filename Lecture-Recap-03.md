# Current and Resistance
One of the main take aways of the previous lecture was the chain of cause and action within the circuits we've looked at. A voltage **source** causes a **current** flow through one or more load **resistors**. And the current through **any** resistor causes a **drop** in voltage across it. Further does *Kirchhoff's Voltage Law* state that the **sum** of all voltage **drops** equals the **source** voltage.

But what is an electrical current and what are resistors after all? Again, the flow model of a water circuit can help explaining. We determined the pressure created by a pump in a water circuit as a propper equivalent to a source voltage. The resulting water flow causes a drop in pressure along the pipes and across a water wheel. We identified this pressure drops as equivalent to the voltage drops across electric resistors. It is therefore obvious that the water flow corrensponds to the electric current.

Water flow is usually defined as the throughput of **volume** per unit **time**. If we choose the count of water **molecules** instead we get pretty close to the definition of the electric current. It is measured in ***Ampere*** named after french physicsist *André-Marie Ampère* (1775-1836). One Ampere is defined as a lot of electrons per second. Or $6.2\times10^{18} \frac{e^-}{s} = 6200000000000000000 \frac{e^-}{s}$ to be precise.

## Filament Resistance
<!--Electrons inside a wire are like dogs beeing dragged on a leash from tree to tree.-->
::: mermaid
xychart-beta
    title "Filament Voltage vs. Current"
    x-axis "Current [mA]" [0, 8, 14, 26, 32, 37]
    y-axis "Voltage [V]" 0 --> 25
    line [0, 1, 5, 10, 16, 22]
:::
::: mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
:::

**The Cauchy-Schwarz Inequality**
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$