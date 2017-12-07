#/usr/bin/env python
# -*- coding:UTF-8 -*-


"""

Este m�dulo fornece uma classe wrapper para ser usada com n�meros de
CPF, que al�m de oferecer um m�todo simples de verifica��o, tamb�m
conta com m�todos para compara��o e convers�o.


>>> a = CPF('56068332551')
>>> b = CPF('560.683.325-51')
>>> c = CPF((1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0))
>>> assert a.valido()
>>> assert b.valido()
>>> assert not c.valido()
>>> assert a == b
>>> assert not b == c
>>> assert not a == c
>>> assert eval(repr(a)) == a
>>> assert eval(repr(b)) == b
>>> assert eval(repr(c)) == c
>>> assert str(a) == \"560.683.325-51\"
>>> assert str(b) == str(a)
>>> assert str(c) == \"123.456.789-00\"

"""




class CPF(object):

    def __init__(self, cpf):
        """Classe representando um n�mero de CPF

        >>> a = CPF('95524361503')
        >>> b = CPF('955.243.615-03')
        >>> c = CPF([9, 5, 5, 2, 4, 3, 6, 1, 5, 0, 3])

        """

        try:
            basestring
        except:
            basestring = (str, unicode)

        if isinstance(cpf, basestring):
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            if not cpf.isdigit():
                raise ValueError("Valor n�o segue a forma xxx.xxx.xxx-xx")
            
        if len(cpf) < 11:
            raise ValueError("O n�mero de CPF deve ter 11 dig�tos")

        self.cpf = map(int, cpf)


    def __getitem__(self, index):
        """Retorna o d�gito em index como string

        >>> a = CPF('95524361503')
        >>> a[9] == '0'
        True
        >>> a[10] == '3'
        True
        >>> a[9] == 0
        False
        >>> a[10] == 3
        False

        """
        return str(self.cpf[index])

    def __repr__(self):
        """Retorna uma representa��o 'real', ou seja:

        eval(repr(cpf)) == cpf

        >>> a = CPF('95524361503')
        >>> print repr(a)
        CPF('95524361503')
        >>> eval(repr(a)) == a
        True
        
        """
        return "CPF('%s')" % ''.join([str(x) for x in self.cpf])

    def __eq__(self, other):
        """Prov� teste de igualdade para n�meros de CPF

        >>> a = CPF('95524361503')
        >>> b = CPF('955.243.615-03')
        >>> c = CPF('123.456.789-00')
        >>> a == b
        True
        >>> a != c
        True
        >>> b != c
        True

        """
        if isinstance(other, CPF):
            return self.cpf == other.cpf
        return False
    
    def __str__(self):
        """Retorna uma string do CPF na forma com pontos e tra�o

        >>> a = CPF('95524361503')
        >>> str(a)
        '955.243.615-03'
        

        """
        d = ((3, "."), (7, "."), (11, "-"))
        s = map(str, self.cpf)
        for i, v in d:
            s.insert(i, v)
        r = ''.join(s)
        return r

    def valido(self):
        """Valida o n�mero de cpf

        >>> a = CPF('95524361503')
        >>> a.valido()
        True
        >>> b = CPF('12345678900')
        >>> b.valido()
        False

        """
        cpf = self.cpf[:9]
        # pegamos apenas os 9 primeiros d�gitos do cpf e geramos os
        # dois d�gitos que faltam
        while len(cpf) < 11:

            r = sum(map(lambda(i,v):(len(cpf)+1-i)*v,enumerate(cpf))) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            cpf.append(f)

        # se o n�mero com os dig�tos faltantes coincidir com o n�mero
        # original, ent�o ele � v�lido
        return bool(cpf == self.cpf)

    def __nonzero__(self):
        """Valida o n�mero de cpf
        
        >>> a = CPF('95524361503')
        >>> bool(a)
        True
        >>> b = CPF('12345678900')
        >>> bool(b)
        False
        >>> if a:
        ...     print 'OK'
        ... 
        OK

        >>> if b:
        ...     print 'OK'
        ... 
        >>>
        """

        return self.valido()



if __name__ == "__main__":

    import doctest, sys
    doctest.testmod(sys.modules[__name__])
