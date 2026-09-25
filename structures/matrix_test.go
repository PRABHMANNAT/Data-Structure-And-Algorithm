package structures
import "testing"
func TestMatrix(t *testing.T){m:=NewMatrix[int](2,2);m.Set(1,1,9);r,c:=m.Dimensions();if m.At(1,1)!=9||r!=2||c!=2{t.Fatal("matrix failed")}}
