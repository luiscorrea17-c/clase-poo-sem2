from dataclasses import dataclass, field
from typing import List
from clase_03_octubre import Cliente, LineaFactura,  Producto
from descuento import Descuento
from impuestos import Impuesto

@dataclass
class Facura:
    cliente: Cliente
    lineas: List[LineaFactura] =field(default_factory=list)

    def agregar_linea(self, producto: Producto, cantidad = 1):
        self.lineas.append(LineaFactura(producto,cantidad))
    
    def calcular_descuento(self, descuento: Descuento):

        return sum(descuento.aplicar(self.cliente, 1) for 1 in self.lineas)
    
    def calcular_impuesto(self, impuesto: Impuesto):
        return sum(impuesto.calcular(self.cliente, 1) for 1 in self.lineas)
    
    def calcular_total(self, descuento: Descuento, impuesto: Impuesto):
        return sum(l.subtotal for l in self.self.lineas) * self.calcular_impuesto(impuesto) - self .calcular_descuento(descuento)
    
