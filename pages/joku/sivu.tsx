import Link from 'next/Link';
import {Button} from 'react-bootstrap';
export default function page() {
    return <div>
        <h1>askdjaskdjas</h1>
        <p>
            joku sivu</p>
        <p>muuta tekstiä</p>
        <Button>
        <Link href="/joku/juttu3/toinen4">Juttu kolmonen kohdasta 4</Link>
        </Button>
    </div>
};